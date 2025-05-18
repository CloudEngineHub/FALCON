from setuptools import find_packages, setup

setup(
    name='falcon',
    version='0.0.1',
    license="MIT",
    packages=find_packages(),
    description='FALCON: Learning Force-Adaptive Humanoid Loco-Manipulation',
    url="https://github.com/LeCAR-Lab/FALCON",  # Update this with your actual repository URL
    python_requires=">=3.8",
    install_requires=[
        "hydra-core>=1.2.0",
        "numpy==1.23.5",
        "rich",
        "ipdb",
        "matplotlib",
        "termcolor",
        "wandb",
        "plotly",
        "tqdm",
        "loguru",
        "meshcat",
        "pynput",
        "scipy",
        "tensorboard",
        "onnx",
        "onnxruntime",
        "opencv-python",
        "joblib",
        "easydict",
        "lxml",
        "numpy-stl",
        "open3d"
    ]
)