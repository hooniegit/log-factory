
def append_lib_dir(relative_path:str):
    import os, sys
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    relative_dir = os.path.join(current_dir, relative_path)
    
    try: 
        sys.path.append(relative_dir)
        return "SUCCEED"
    
    except Exception as e:
        return f"FAILED - {e}"


def return_abs_dir(relative_path:str):
    import os
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    relative_dir = os.path.join(current_dir, relative_path)
    
    return relative_dir


if __name__ == "__main__":
    # test - append_lib_dir
    result = append_lib_dir(relative_path = "./")
    print(result)
    
    # test - return_abs_dir
    absolute_dir = return_abs_dir(relative_path = "./")
    print(absolute_dir)
