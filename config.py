import torch

BATCH_SIZE = 2 # Increase / decrease according to GPU memeory.
RESIZE_TO = 640 # Base image resolution transforms.
NUM_EPOCHS = 75 # Number of epochs to train for.
NUM_WORKERS = 4 # Number of parallel workers for data loading.
LR = 0.001 # Initial learning rate. 
DEVICE = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

# Keep `resolutions=None` for not using multi-resolution training,
# else it will be 50% lower than base `RESIZE_TO`, then base `RESIZE_TO`, 
# and 50% higher than base `RESIZE_TO`
RESOLUTIONS = [
    (int(RESIZE_TO/2), int(RESIZE_TO/2)), 
    (RESIZE_TO, RESIZE_TO), 
    (int(RESIZE_TO*2), int(RESIZE_TO*2))
]
# RESOLUTIONS = None

# Training images and XML files directory.
TRAIN_IMG = 'data/aquarium/train'
TRAIN_ANNOT = 'data/aquarium/train'
# Validation images and XML files directory.
VALID_IMG = 'data/aquarium/valid'
VALID_ANNOT = 'data/aquarium/valid'
# Classes: 0 index is reserved for background.
CLASSES = [
    '__background__',
    'fish', 
    'jellyfish', 
    'penguin',
    'shark', 
    'puffin', 
    'stingray',
    'starfish'
]

NUM_CLASSES = len(CLASSES)

# Whether to visualize images after crearing the data loaders.
VISUALIZE_TRANSFORMED_IMAGES = False

# Automatic Mixed Preicision?
AMP = True

# If kept None, it will be incremental as exp1, exp2,
# else it will be name provided.
PROJECT_NAME = 'retinanet' 