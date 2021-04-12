>>> from io import BytesIO                                                                               │]\PYTHON  REST_API  codes  educa  introducing-python  project_js  udemy                                 
>>> from PIL import Image                                                                                │mechanic@mechanic:~/dev/training$ mkdir python_training                                                 
>>> import sys                                                                                           │mechanic@mechanic:~/dev/training$ ls
>>>                                                                                                      │PYTHON  REST_API  codes  educa  introducing-python  project_js  python_training  udemy                  
>>>                                                                                                      │mechanic@mechanic:~/dev/training$ cd python_training/                                                   
>>> def data_to_img(data):                                                                               │mechanic@mechanic:~/dev/training/python_training$ echo "# python_training" >> README.md                 
...     fp = BytesIO(data)                                                                               │mechanic@mechanic:~/dev/training/python_training$ git init                                              
...     return Image.open(fp)                                                                            │Initialized empty Git repository in /home/mechanic/dev/training/python_training/.git/                   
...                                                                                                      │mechanic@mechanic:~/dev/training/python_training$ git add README.md                                     
>>> def img_to_data(img, fmt=None):                                                                      │mechanic@mechanic:~/dev/training/python_training$ git commit -m "first commit"                          
...     fp = BytesIO()                                                                                   │[master (root-commit) 51acafc] first commit
...     if not fmt:                                                                                      │ 1 file changed, 1 insertion(+)
...             fmt = img.format                                                                         │ create mode 100644 README.md
...     img.save(fp, fmt)                                                                                │mechanic@mechanic:~/dev/training/python_training$ git branch -M main                                    
...     return fp.getvalue()                                                                             │mechanic@mechanic:~/dev/training/python_training$ git remote add origin git@github.com:furkalokbu/python_
...                                                                                                      │training.git
>>> def convert_image(data, fmt=None):                                                                   │mechanic@mechanic:~/dev/training/python_training$ git push -u origin main                               
...     img = data_to_img(data)                                                                          │Enumerating objects: 3, done.
...     return img_to_data(img, fmt)                                                                     │Counting objects: 100% (3/3), done.
...                                                                                                      │Writing objects: 100% (3/3), 228 bytes | 228.00 KiB/s, done.                                            
>>> def get_file_data(name):                                                                             │Total 3 (delta 0), reused 0 (delta 0)
...     img = Image.open(name)                                                                           │To github.com:furkalokbu/python_training.git
...     print('img', img, img.format)                                                                    │ * [new branch]      main -> main
...     return img_to_data(img)                                                                          │Branch 'main' set up to track remote branch 'main' from 'origin'.                                       
...                                                                                                      │mechanic@mechanic:~/dev/training/python_training$ vim convert_image.py                                  
>>> if __name__ == "__main__":                                                                           │mechanic@mechanic:~/dev/training/python_training$ 
...     for name in sys.argv[1:]:                                                                        ├─────────────────────────────────────────────────────────────────────────────────────────────────────────
...             data = get_file_data(name)                                                               │mechanic@mechanic:~/dev/training/PYTHON$
...             print('in', len(data), data[:10])                                                        │
...             for fmt in ('gif', 'png', 'jpeg'):                                                       │
...                     out_data = convert_image(data, fmt) 