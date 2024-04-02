import mmcv
import matplotlib.pyplot as plt
from mmagic.apis import MMagicInferencer

# Create a MMagicInferencer instance and infer
img = 'https://github-production-user-asset-6210df.s3.amazonaws.com/49083766/245713512-de973677-2be8-4915-911f-fab90bb17c40.jpg'
result_out_dir = './resources/output/colorization/tutorial_colorization_res.png'
editor = MMagicInferencer('inst_colorization')
results = editor.infer(img=img, result_out_dir=result_out_dir)