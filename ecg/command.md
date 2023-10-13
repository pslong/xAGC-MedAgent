python3 [commandPath] <dataset>.json <model>.hdf5


test files path
/usr/local/software/ecg/zhangsanA.json
/usr/local/software/ecg/zhangsanN.json

model path
/usr/local/software/ecg/ecg-model/0.406-0.867-020-0.264-0.907.h5


command path
/usr/local/software/ecg/xAGC-MedAgent/ecg/ecg

__init__.py  analyze.py  load.py  network.py  predict.py  train.py  util.py


python3 /usr/local/software/ecg/xAGC-MedAgent/ecg/ecg/predict.py /usr/local/software/ecg/zhangsanA.json /usr/local/software/ecg/ecg-model/0.406-0.867-020-0.264-0.907.h5

python /home/ubuntu/aimodel/ecg/ecg/predict.py /home/ubuntu/aimodel/ecg/dev-N.json /home/ubuntu/aimodel/ecg/saved/cinc17/1696514528-820/0.406-0.867-020-0.264-0.907.h5

python /home/ubuntu/aimodel/ecg/ecg/predict.py /home/ubuntu/aimodel/ecg/dev-N.json /home/ubuntu/aimodel/ecg/saved/cinc17/1696514528-820/0.406-0.867-020-0.264-0.907.h5



scp

scp ubuntu@43.156.37.199:/home/ubuntu/aimodel/ecg/saved/cinc17/1696514528-820/preproc.bin /Users/4pmtong/Desktop/ai-model/ecg-model/preproc.bin

scp -i "team036.pem"  /Users/4pmtong/Desktop/ai-model/ecg-model/preproc.bin ubuntu@ec2-43-192-154-106.cn-northwest-1.compute.amazonaws.com.cn:/usr/local/software/ecg/ecg-model/preproc.bin

scp /Users/4pmtong/Desktop/ai-model/dirichlet_model.zip ubuntu@43.156.37.199:/home/ubuntu/aimodel/dirichlet_model.zip



