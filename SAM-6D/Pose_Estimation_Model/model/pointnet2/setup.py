import os
from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CUDAExtension

# 获取当前绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))
include_path = os.path.join(current_dir, '_ext_src/include')

setup(
    name='pointnet2',
    ext_modules=[
        CUDAExtension(
            'pointnet2._ext',
            sources=[
                '_ext_src/src/ball_query.cpp',
                '_ext_src/src/ball_query_gpu.cu',
                '_ext_src/src/bindings.cpp',
                '_ext_src/src/group_points.cpp',
                '_ext_src/src/group_points_gpu.cu',
                '_ext_src/src/interpolate.cpp',
                '_ext_src/src/interpolate_gpu.cu',
                '_ext_src/src/sampling.cpp',
                '_ext_src/src/sampling_gpu.cu',
            ],
            include_dirs=[include_path],  # 确保使用绝对路径
            extra_compile_args={
                'cxx': ['-O3', '-std=c++17'],
                'nvcc': ['-O3', '-std=c++17']
            }
        )
    ],
    cmdclass={'build_ext': BuildExtension}
)