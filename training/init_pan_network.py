import sys
sys.path.append('/space2/water/ctx/python')
import caffe

fusion_net = caffe.Net('part_action_with_ctx_trainval.prototxt', caffe.TEST)

model_def = 'ResNet-50-deploy.prototxt'
model_weight = 'ResNet-50-model.caffemodel'
net = caffe.Net(model_def, model_weight, caffe.TEST)

for layer_name, param in net.params.iteritems():
    n_params = len(param)
    for i in range(n_params):
        fusion_net.params['app_{}'.format(layer_name)][i].data[...] = param[i].data[...]
        fusion_net.params['act_{}'.format(layer_name)][i].data[...] = param[i].data[...]
    

fusion_net.save('init_part_action.caffemodel')
