import sys
import pandas
import numpy
import tensorflow as tf
import tensorflow_probability as tfp
from MkTFDataset import MkTFDataset
from linear_classification_model_cpu import LinearClassificationModel
from func_factory_lbfgs_cpu_pr2 import FunctionFactory

filename_default = 'train_file__TagX.tsv'
#filename_default = 'train_file__testsample.tsv'
outfn_default = 'model_d4.txt'

def test_access(model, data_train):
    for irow in data_train:
        print('testing access')
        print(model(irow))
        break

def train(inp_para):
    dim_feat = 112244889
    batch_size = 65536
    #init_model_weights = numpy.zeros((dim_feat+1,), numpy.float64)
    #init_model_weights = tf.Variable(numpy.zeros((dim_feat+1,), numpy.float64), trainable=True)

    inpfilename = inp_para[1] if (len(inp_para)>1 and len(inp_para[1])>0) else filename_default
    filename = '/data/{}'.format(inpfilename)
    outfn = inp_para[2] if (len(inp_para)>2 and len(inp_para[2])>0) else outfn_default

    print('filename', filename)
    print('outfn', outfn)

    ds_train = MkTFDataset([filename])
    ds_train.init_traindata(batch_size, 1.0)
    data_train = ds_train.dataset_train

    model = LinearClassificationModel(dim_feat)
    test_access(model, data_train)

    func_obj = FunctionFactory(model, data_train, dim_feat)
    func = func_obj.gen_function()
    init_model_weights = tf.dynamic_stitch(func.idx, model.trainable_variables)

    results = tfp.optimizer.lbfgs_minimize(
        value_and_gradients_function=func,
        initial_position=init_model_weights,
        max_iterations=1000,
        parallel_iterations=1,
        num_correction_pairs=6,
        x_tolerance=1.0e-16,
        tolerance=1e-5,
        f_relative_tolerance=1e-10,
        max_line_search_iterations=40,
        f_absolute_tolerance=0.0001)

    outw = results.position.numpy()
    with open(outfn, 'w') as fw:
        for iv in enumerate(outw):
            if iv[1]!=0.:
                fw.write('{}\n'.format(iv))

    return data_train, model, results

if __name__ == '__main__':
    print('sys.argv=', sys.argv)
    if 'train_lbfgs_cpu_try2.py' in sys.argv[0]:
        train(sys.argv)
