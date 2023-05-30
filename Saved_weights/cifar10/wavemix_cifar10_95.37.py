import torch, wavemix
from wavemix.classification import WaveMix

model = WaveMix(
    num_classes = 10,
    depth = 8,
    mult = 2,
    ff_channel = 320,
    final_dim = 320,
    dropout = 0.5,
    level=1,
    initial_conv = 'strided',
    stride = 1

)



url = 'https://huggingface.co/cloudwalker/wavemix/resolve/main/Saved_Models_Weights/cifar10/cifar10_95.37.pth'

model.load_state_dict(torch.hub.load_state_dict_from_url(url))