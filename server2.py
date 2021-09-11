from socket import *
import base64
import json
from InferFace import InferFace
import cv2
import numpy as np


file_path = r"./config/face.json"
with open(file_path, "r", encoding="UTF-8") as fr:
    config = json.load(fr)
im_size = config["global"]["im_size"]
config["train"]["model_file_path"] = r"./model/ResNet50-29-0.97.hdf5"
inferFace = InferFace(config)


def main():
    HOST = '127.0.0.1'
    PORT = 9999
    BUFSIZ = 1024*20
    ADDR = (HOST, PORT)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)
    while True:
        rec_d = bytes([])
        print('waiting for connection...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('...connected from:', addr)
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            if not data or len(data) == 0:
                break
            else:
                rec_d = rec_d + data
        rec_d = base64.b64decode(rec_d)
        np_arr = np.fromstring(rec_d, np.uint8)

        image = cv2.imdecode(np_arr, 1)
        image = inferFace.pre_process_face(image)
        label, score = inferFace.infer_model(image)

        tcpCliSock.send(label.encode())
        # tcpCliSock.send("返回值")
        tcpCliSock.close()
    tcpSerSock.close()

if __name__ == "__main__":
    main()
