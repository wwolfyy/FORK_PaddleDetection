import subprocess, os, time
# import fitz
# import paddle
import debugpy

configfile = "../configs/picodet/legacy_model/application/layout_analysis/krcase_layout_train.yml"
# slim_configfile = " ../configs/picodet/legacy_model/application/layout_analysis/krcase_layout_distill.yml"

inference_datafolder = './testdata'
# testdoc_img_folder = 'adobe_대법원_2020도1007_판결서'
testdoc_img_folder = 'CONVERTED_PNG'
weight2use = '20240503'
output_dir = './testresults'
output_path = f'{output_dir}/{weight2use}/{testdoc_img_folder}'

if not os.path.exists(output_path):
    os.makedirs(output_path)

command = (
    "python3 ../tools/infer.py",
    f"-c {configfile}",
    # f"--slim_config {slim_configfile}",
    f"--infer_dir={inference_datafolder}/{testdoc_img_folder}",
    # f"--infer_img={inference_datafolder}/{testdoc_img_folder}/adobe_table_광주지법_2019구합10788_판결서_0.png",
    f"-o weights=./trained_weights/output_{weight2use}/best_model/model.pdparams",
    "--draw_threshold=0.5",
    # "use_gpu=true",
    # "--use_vdl=True",
    # "--vdl_log_dir=./vdl_log_test",
    # f"--output_dir={output_path}"
    )
command = " ".join(command)
print(command)

debugpy.listen(("localhost", 5678))
time.sleep(5)
debugpy.wait_for_client()


subprocess.call(command, shell=True)
