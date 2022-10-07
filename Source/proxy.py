from unittest import mock

camera_mock = mock.MagicMock(
    brightness=10,
    contrast=10,
    saturation=10,
    sharpness=10,
    IMAGE_EFFECTS={
        'none': None,
        'off': None,
        '1': None,
    },
    FLASH_MODES={
        'off': None,
        'auto': None,
        '1': None,
    },
    METER_MODES={
        'off': None,
    },
    EXPOSURE_MODES={
        'off': None,
        'auto': None,
        '1': None,
        '2': None,
    },
    DRC_STRENGTHS={
        'off': None,
        '1': None,
    },
    AWB_MODES={
        'off': None,
        'auto': None,
        '1': None,
        '2': None,
    },
    still_stats=False,
)

try:
    import picamera
except ImportError:
    picamera = mock.MagicMock()
    picamera.PiCamera = lambda *args, **kwargs: camera_mock
