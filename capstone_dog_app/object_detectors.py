import cv2
import torch
import numpy as np
from PIL import ImageFile, Image
import torchvision.transforms as transforms
ImageFile.LOAD_TRUNCATED_IMAGES = True

# returns "True" if face is detected in image stored at img_path
def face_detector( img_path, face_cascade):
    """This fuction detects the presence or absence
    of face(s) in an image
        **args: path to an image
        **returns: (bool) True/False
    """
    img = cv2.imread( img_path )
    gray = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY )
    faces = face_cascade.detectMultiScale( gray )
    if len( faces ) > 0:
        return True
    else:
        return False


### returns "True" if a dog is detected in the image stored at img_path
def dog_detector( img_path, model, dog_model ):
    """This fuction detects the presence or absence
    of a dog in an image
        **args: img_path - path to an image
                model - trained classifier
                
        **returns: (bool) True/False
    """


    def model_predict( img_path, model, use_cuda=False ):
        '''
        Use pre-trained VGG-16 model to obtain index corresponding to 
        predicted ImageNet class for image at specified path
        
        Args:
            img_path: path to an image
            model: trained classifier
            
        Returns:
            Index corresponding to VGG-16 model's prediction
        '''
        
        ## Load and pre-process an image from the given img_path
        ## Return the *index* of the predicted class for that image
        # Load in the image and convert to rgb
        img = Image.open(img_path).convert('RGB')
        
        # transforming image
        transform = transforms.Compose([transforms.Resize(256),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize(mean=[0.485, 0.456, 0.406],#see https://pytorch.org/docs/stable/torchvision/models.html
                                                            std=[0.229, 0.224, 0.225])])#for how they are obtained from the images 
        img = transform(img)
        
        # move model to cuda if available
        if use_cuda:
            model = model.cuda()
            img = img.cuda()
        else:
            model = model.cpu()
        
        # Unsqueezing to add artificial dimension
        img = img.unsqueeze(0)
        
        # getting predictions, set model to evaluation
        model.eval()
        with torch.no_grad():
            output = model.forward(img)
            output = output.cpu()
            
        _, predicted_class_idx = torch.max(output, 1)
                                        
        return predicted_class_idx # predicted class index

    ## Detect Dogs
    dog_label = model_predict( img_path=img_path, model=dog_model )
    if dog_label in torch.LongTensor( np.arange(151, 269, 1) ):
        return True
    else:
        return False # true/false


def detect_image( img_path, breed, dog_model, model, face_cascade):

    ## handle cases for a human face, dog, and neither
    
    # checks for human faces in image
    has_face = face_detector(img_path=img_path, face_cascade=face_cascade)
    # Checks for dog in image
    is_dog = dog_detector(img_path=img_path, dog_model=dog_model, model=model)

    if has_face:
        f_1 = "Hello Human!"
        f_2 = 'You look like the "' + breed + '" dog breed!'
        return f_1, f_2
    if is_dog:
        d_1 = "Hello Furry Friend!"
        d_2 = 'Your predicted breed is..........\n' + breed
        return d_1, d_2
    else:
        n_1 = "Oh Dear........"
        n_2 = "This image has neither a dog nor a human in it... Let's try another one."
        return n_1, n_2