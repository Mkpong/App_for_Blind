import torch
import yaml
from glob import glob

if torch.cuda.is_available():
    DEVICE = torch.device('cuda')
else:
    DEVICE = torch.device('cpu')
print("Using PyTorch version : ", torch.__version__, 'Device : ', DEVICE)

data = yaml.load(open('./Snack/data.yaml', 'r'), Loader=yaml.Loader)

train_img_list = glob('/home/leeej/CISLab/WinterPj/Snack/train/images/*.jpg')
#print(len(train_img_list)) # 1677

valid_img_list = glob('/home/leeej/CISLab/WinterPj/Snack/valid/images/*.jpg')
#print(len(valid_img_list)) # 239

with open('./Snack/train.txt', 'w') as f:
    f.write('\n'.join(train_img_list) + '\n')
with open('./Snack/val.txt', 'w') as f:
    f.write('\n'.join(valid_img_list) + '\n')
    
data['train'] = '/home/leeej/CISLab/WinterPj/Snack/train.txt'
data['val'] = '/home/leeej/CISLab/WinterPj/Snack/val.txt'

with open('./Snack/data.yaml', 'w') as f:
    yaml.dump(data, f, default_flow_style=False)
    
with open('./Snack/data.yaml', 'r') as f:
    for i in f:
        i = i.rstrip()
        print(i)
