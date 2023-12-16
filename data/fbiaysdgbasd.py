from search import counter_test
import torch



#
# input = torch.rand(2,2,2)
# input = torch.rand(1)
input = torch.Tensor([0.8945])
print('input::', input)


BOO = counter_test.counter_ones_for_params_version_3(input)
print('BOO::', BOO)

float2bin = counter_test.float2bin(input)
print('float2bin::', float2bin)

bin2float = counter_test.bin2float(float2bin)
print('bin2float::', bin2float)


number_of_ones = counter_test.number_of_ones(float2bin)
print('number_of_ones::', number_of_ones)

counter_ones_version_2 = counter_test.counter_ones_version_2(input)
print('counter_ones_version_2::', counter_ones_version_2)

counter_ones_for_params = counter_test.counter_ones_for_params(input)
print('counter_ones_for_params::', counter_ones_for_params)


counter_ones = counter_test.counter_ones(input)
print('counter_ones::', counter_ones)

