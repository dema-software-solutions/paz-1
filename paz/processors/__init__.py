# imports are done directly to keep user's auto-complete clean

from .detection import SquareBoxes2D
from .detection import DenormalizeBoxes2D
from .detection import RoundBoxes2D
from .detection import ClipBoxes2D
from .detection import FilterClassBoxes2D
from .detection import CropBoxes2D
from .detection import ToBoxes2D
from .detection import MatchBoxes
from .detection import EncodeBoxes
from .detection import DecodeBoxes
from .detection import NonMaximumSuppressionPerClass
from .detection import FilterBoxes
from .detection import OffsetBoxes2D
from .detection import CropImage

from .draw import DrawBoxes2D
from .draw import DrawKeypoints2D
from .draw import DrawBoxes3D
from .draw import DrawRandomPolygon
from .draw import DrawPose6D

from .image import CastImage
from .image import SubtractMeanImage
from .image import AddMeanImage
from .image import NormalizeImage
from .image import DenormalizeImage
from .image import LoadImage
from .image import RandomSaturation
from .image import RandomBrightness
from .image import RandomContrast
from .image import RandomHue
from .image import ResizeImage
from .image import ResizeImages
from .image import RandomImageBlur
from .image import RandomGaussianBlur
from .image import RandomFlipImageLeftRight
from .image import ConvertColorSpace
from .image import ShowImage
from .image import ImageDataProcessor
from .image import AlphaBlending
from .image import RandomShapeCrop
from .image import RandomImageCrop
from .image import MakeRandomPlainImage
from .image import ConcatenateAlphaMask
from .image import BlendRandomCroppedBackground
from .image import AddOcclusion
from .image import ImageToNormalizedDeviceCoordinates
from .image import NormalizedDeviceCoordinatesToImage
from .image import ReplaceLowerThanThreshold
from .image import GetNonZeroArguments
from .image import GetNonZeroValues

from .image import BGR_IMAGENET_MEAN
from .image import RGB_IMAGENET_MEAN

from .renderer import Render

from .geometric import RandomFlipBoxesLeftRight
from .geometric import ToImageBoxCoordinates
from .geometric import ToNormalizedBoxCoordinates
from .geometric import RandomSampleCrop
from .geometric import Expand
from .geometric import ApplyTranslation
from .geometric import RandomTranslation
from .geometric import RandomKeypointTranslation
from .geometric import RandomKeypointRotation
from .geometric import RandomRotation
from .geometric import TranslateImage

from .keypoints import ChangeKeypointsCoordinateSystem
from .keypoints import DenormalizeKeypoints
from .keypoints import NormalizeKeypoints
from .keypoints import PartitionKeypoints
from .keypoints import ProjectKeypoints
from .keypoints import RemoveKeypointsDepth
from .keypoints import TranslateKeypoints
from .keypoints import DenormalizeKeypoints2D
from .keypoints import NormalizeKeypoints2D
from .keypoints import ArgumentsToImageKeypoints2D

from .standard import ControlMap
from .standard import ExpandDomain
from .standard import CopyDomain
from .standard import ExtendInputs
from .standard import SequenceWrapper
from .standard import Predict
from .standard import ToClassName
from .standard import ExpandDims
from .standard import BoxClassToOneHotVector
from .standard import Squeeze
from .standard import Copy
from .standard import Lambda
from .standard import UnpackDictionary
from .standard import WrapOutput
from .standard import Concatenate
from .standard import SelectElement
from .standard import StochasticProcessor
from .standard import Stochastic
from .standard import UnwrapDictionary
from .standard import Scale

from .pose import SolvePNP
from .pose import SolveChangingObjectPnPRANSAC

from .groups import ToAffineMatrix
from .groups import RotationVectorToQuaternion
from .groups import RotationVectorToRotationMatrix

from ..backend.image.opencv_image import RGB2BGR
from ..backend.image.opencv_image import BGR2RGB
from ..backend.image.opencv_image import RGB2GRAY
from ..backend.image.opencv_image import RGB2HSV
from ..backend.image.opencv_image import HSV2RGB

from ..backend.keypoints import UPNP
from ..backend.keypoints import LEVENBERG_MARQUARDT

from ..backend.image.draw import GREEN
from ..backend.image.draw import FONT
from ..backend.image.draw import LINE

from ..abstract import Processor
from ..abstract import SequentialProcessor

TRAIN = 0
VAL = 1
TEST = 2
