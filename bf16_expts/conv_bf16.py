import torch
import time

def time_copy(src, dst, num_iterations):
    copy_start_time = time.time()
    for i in range(num_iterations):
        
        # Python warning:
        # To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or
        # sourceTensor.clone().detach().requires_grad_(True), rather than tensor.new_tensor(sourceTensor).
        b = dst.new_tensor(src)
    
    copy_end_time = time.time()
    
    copy_elapsed_time = copy_end_time - copy_start_time
    
    avg_copy_time = copy_elapsed_time / num_iterations
    print("\nCopy using dst.new_tensor(src) ")
    print(f"Src : {src.shape}, {src.dtype}")
    print(f"Dst: {dst.shape}, {dst.dtype}")
    print(f"Avg .new_tensor() time: {avg_copy_time} sec")
    
    
def time_clone(src, dst, num_iterations):
    type_start_time = time.time()
    for i in range(num_iterations):
        
        # Python warning:
        # To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or
        # sourceTensor.clone().detach().requires_grad_(True), rather than tensor.new_tensor(sourceTensor).
        # dst = src.clone()
        dst = src.type(dst.dtype)
    
    type_end_time = time.time()
    
    type_elapsed_time = type_end_time - type_start_time
    
    avg_type_time = type_elapsed_time / num_iterations
    
    print("\nConvert using (src.type(dst.dtype)) ")
    print(f"Src : {src.shape}, {src.dtype}")
    print(f"Dst: {dst.shape}, {dst.dtype}")
    print(f"Avg .type time: {avg_type_time} sec")

    
def time_explicit_conv(src, dst, num_iterations):
    explicit_conv_start_time = time.time()
    
    for i in range(num_iterations):
        dst = src.bfloat16()
    explicit_conv_end_time = time.time()

    explicit_conv_elapsed_time = explicit_conv_end_time - explicit_conv_start_time
    avg_expl_conv_time = explicit_conv_elapsed_time / num_iterations
    
    print("\nConvert using src.bfloat16()")
    print(f"Src : {src.shape}, {src.dtype}")
    print(f"Dst: {dst.shape}, {dst.dtype}")
    print(f"Avg .bfloat16() time: {avg_expl_conv_time} sec")
    
    
if __name__ == '__main__':
    
    num_iterations = 1000
    src = torch.randn((1000, 1000), dtype=torch.float32)
    dst = torch.ones((1000, 1000), dtype=torch.bfloat16)
    
    time_copy(src, dst, num_iterations)
    
    time_clone(src, dst, num_iterations)
    
    time_explicit_conv(src, dst, num_iterations)