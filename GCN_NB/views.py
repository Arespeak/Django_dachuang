from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, reverse
from GCN_NB.Process_gcn.predict_cut import predict_cut
from GCN_NB.Process_gcn.Parameters import Parameters as ppm

def index(request):
    if request.method == 'GET':
        return render(request, 'Web/index.html')
    else:
        input_text = request.POST.get('input_text', '')
        print(input_text)
        output_text = Process_cut(input_text)

        output_text_real=""
        for one in output_text:
            output_text_real+=one

        return render(request, 'Web/fenci.html', {'result': output_text[0], 'input_text':input_text})

# def fenci(request):
#     if request.method == 'GET':
#         return render(request, 'Web/fenci.html', {'result': '顾彤傻逼'})

def Process_cut(input_str):
    savaTxt(input_str)
    out_str = predict_cut()
    return out_str


def savaTxt(res):
    with open('D:/大创/qianduan/GCN_BiLSTM_CRF/GCN_NB/Process_gcn/data/eva.txt', 'w', encoding='utf-8') as fw:
            fw.write(res)
