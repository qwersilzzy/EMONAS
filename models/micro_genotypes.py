from collections import namedtuple

Genotype = namedtuple('Genotype', 'normal normal_concat reduce reduce_concat')

PRIMITIVES = [
    'none',
    'max_pool_3x3',
    'avg_pool_3x3',
    'skip_connect',
    'sep_conv_3x3',
    'sep_conv_5x5',
    'dil_conv_3x3',
    'dil_conv_5x5'
]

NASNet = Genotype(
    normal=[
        ('sep_conv_5x5', 1),
        ('sep_conv_3x3', 0),
        ('sep_conv_5x5', 0),
        ('sep_conv_3x3', 0),
        ('avg_pool_3x3', 1),
        ('skip_connect', 0),
        ('avg_pool_3x3', 0),
        ('avg_pool_3x3', 0),
        ('sep_conv_3x3', 1),
        ('skip_connect', 1),
    ],
    normal_concat=[2, 3, 4, 5, 6],
    reduce=[
        ('sep_conv_5x5', 1),
        ('sep_conv_7x7', 0),
        ('max_pool_3x3', 1),
        ('sep_conv_7x7', 0),
        ('avg_pool_3x3', 1),
        ('sep_conv_5x5', 0),
        ('skip_connect', 3),
        ('avg_pool_3x3', 2),
        ('sep_conv_3x3', 2),
        ('max_pool_3x3', 1),
    ],
    reduce_concat=[4, 5, 6],
)

AmoebaNet = Genotype(
    normal=[
        ('avg_pool_3x3', 0),
        ('max_pool_3x3', 1),
        ('sep_conv_3x3', 0),
        ('sep_conv_5x5', 2),
        ('sep_conv_3x3', 0),
        ('avg_pool_3x3', 3),
        ('sep_conv_3x3', 1),
        ('skip_connect', 1),
        ('skip_connect', 0),
        ('avg_pool_3x3', 1),
    ],
    normal_concat=[4, 5, 6],
    reduce=[
        ('avg_pool_3x3', 0),
        ('sep_conv_3x3', 1),
        ('max_pool_3x3', 0),
        ('sep_conv_7x7', 2),
        ('sep_conv_7x7', 0),
        ('avg_pool_3x3', 1),
        ('max_pool_3x3', 0),
        ('max_pool_3x3', 1),
        ('conv_7x1_1x7', 0),
        ('sep_conv_3x3', 5),
    ],
    reduce_concat=[3, 4, 6]
)

DARTS = Genotype(
    normal=[
        ('sep_conv_3x3', 0),
        ('sep_conv_3x3', 1),
        ('sep_conv_3x3', 0),
        ('sep_conv_3x3', 1),
        ('sep_conv_3x3', 1),
        ('skip_connect', 0),
        ('skip_connect', 0),
        ('dil_conv_3x3', 2)
    ],
    normal_concat=[2, 3, 4, 5],
    reduce=[
        ('max_pool_3x3', 0),
        ('max_pool_3x3', 1),
        ('skip_connect', 2),
        ('max_pool_3x3', 1),
        ('max_pool_3x3', 0),
        ('skip_connect', 2),
        ('skip_connect', 2),
        ('max_pool_3x3', 1)
    ],
    reduce_concat=[2, 3, 4, 5]
)

ENAS = Genotype(
    normal=[
        ('sep_conv_3x3', 1),
        ('skip_connect', 1),
        ('sep_conv_5x5', 1),
        ('skip_connect', 0),
        ('avg_pool_3x3', 0),
        ('sep_conv_3x3', 1),
        ('sep_conv_3x3', 0),
        ('avg_pool_3x3', 0),
        ('sep_conv_5x5', 1),
        ('avg_pool_3x3', 0)
    ],
    normal_concat=[2, 3, 4, 5, 6],
    reduce=[
        ('sep_conv_5x5', 0),
        ('avg_pool_3x3', 1),
        ('sep_conv_3x3', 1),
        ('avg_pool_3x3', 1),
        ('avg_pool_3x3', 1),
        ('sep_conv_3x3', 1),
        ('sep_conv_5x5', 4),
        ('avg_pool_3x3', 1),
        ('sep_conv_3x3', 5),
        ('sep_conv_5x5', 0)
    ],
    reduce_concat=[2, 3, 6]
)

NSGANet = Genotype(
    normal=[
        ('skip_connect', 0),
        ('max_pool_3x3', 0),
        ('dil_conv_5x5', 0),
        ('max_pool_3x3', 0),
        ('dil_conv_5x5', 1),
        ('sep_conv_3x3', 3),
        ('max_pool_3x3', 1),
        ('sep_conv_5x5', 3),
        ('sep_conv_3x3', 1),
        ('sep_conv_3x3', 0)
    ],
    normal_concat=[2, 4, 5, 6],
    reduce=[
        ('avg_pool_3x3', 0),
        ('sep_conv_3x3', 1),
        ('dil_conv_3x3', 1),
        ('max_pool_3x3', 0),
        ('skip_connect', 2),
        ('dil_conv_5x5', 1),
        ('skip_connect', 2),
        ('avg_pool_3x3', 1),
        ('dil_conv_5x5', 1),
        ('dil_conv_3x3', 1)
    ],
    reduce_concat=[3, 4, 5, 6]
)





# test2333 = Genotype(
#     normal=[
#         ('sep_conv_7x7', 0),
#         ('dil_conv_5x5', 1),
#         ('sep_conv_7x7', 0),
#         ('sep_conv_7x7', 0),
#         ('avg_pool_3x3', 0),
#         ('avg_pool_3x3', 0),
#         ('sep_conv_5x5', 1),
#         ('dil_conv_3x3', 2),
#         ('dil_conv_5x5', 1),
#         ('avg_pool_3x3', 4)
#     ],
#     normal_concat=[3, 5, 6],
#     reduce=[
#             ('sep_conv_7x7', 0),
#             ('dil_conv_5x5', 1),
#             ('avg_pool_3x3', 0),
#             ('max_pool_3x3', 0),
#             ('dil_conv_3x3', 3),
#             ('avg_pool_3x3', 2),
#             ('max_pool_3x3', 2),
#             ('dil_conv_5x5', 2),
#             ('sep_conv_7x7', 3),
#             ('avg_pool_3x3', 2)
#     ],
#     reduce_concat=[4, 5, 6]
# )

test2333 = Genotype(
    normal=[
        ('sep_conv_7x7', 1),
        ('sep_conv_5x5', 0),
        ('skip_connect', 1),
        ('dil_conv_3x3', 2),
        ('conv_7x1_1x7', 2),
        ('avg_pool_3x3', 1),
        ('sep_conv_5x5', 3),
        ('sep_conv_5x5', 4),
        ('skip_connect', 3),
        ('conv_7x1_1x7', 1)
    ],
    normal_concat=[5, 6],
    reduce=[('dil_conv_3x3', 0),
            ('conv_7x1_1x7', 0),
            ('dil_conv_5x5', 1),
            ('avg_pool_3x3', 2),
            ('sep_conv_5x5', 2),
            ('max_pool_3x3', 2),
            ('sep_conv_3x3', 4),
            ('dil_conv_5x5', 1),
            ('max_pool_3x3', 3),
            ('sep_conv_5x5', 4)
            ],
    reduce_concat=[5, 6]
)


# # 20230116 pareto front plot for evolutionary micro search archi 100 epoch 20
res_0_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 2), ('dil_conv_5x5', 2), ('avg_pool_3x3', 3), ('max_pool_3x3', 3), ('skip_connect', 1), ('dil_conv_5x5', 3), ('avg_pool_3x3', 3), ('avg_pool_3x3', 4)], normal_concat=[5, 6], reduce=[('avg_pool_3x3', 1), ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 0), ('dil_conv_3x3', 3), ('avg_pool_3x3', 2), ('max_pool_3x3', 2), ('sep_conv_3x3', 0), ('dil_conv_3x3', 4), ('sep_conv_5x5', 0)], reduce_concat=[5, 6])

res_1_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 2), ('dil_conv_5x5', 2), ('avg_pool_3x3', 3), ('max_pool_3x3', 3), ('skip_connect', 1), ('dil_conv_5x5', 3), ('avg_pool_3x3', 3), ('avg_pool_3x3', 4)], normal_concat=[5, 6], reduce=[('avg_pool_3x3', 1), ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 0), ('dil_conv_3x3', 3), ('skip_connect', 0), ('sep_conv_5x5', 0), ('sep_conv_3x3', 0), ('dil_conv_3x3', 5), ('sep_conv_5x5', 0)], reduce_concat=[4, 6])

res_2_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('max_pool_3x3', 3), ('skip_connect', 2), ('dil_conv_5x5', 3), ('avg_pool_3x3', 3), ('avg_pool_3x3', 5)], normal_concat=[4, 6], reduce=[('avg_pool_3x3', 1), ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), ('avg_pool_3x3', 0), ('avg_pool_3x3', 0), ('skip_connect', 3), ('sep_conv_7x7', 2), ('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 0)], reduce_concat=[4, 5, 6])

res_3_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('max_pool_3x3', 3), ('skip_connect', 2), ('dil_conv_5x5', 3), ('max_pool_3x3', 3), ('sep_conv_3x3', 4)], normal_concat=[5, 6], reduce=[('dil_conv_3x3', 0), ('skip_connect', 0), ('sep_conv_5x5', 1), ('avg_pool_3x3', 0), ('avg_pool_3x3', 0), ('skip_connect', 0), ('sep_conv_5x5', 2), ('avg_pool_3x3', 0), ('max_pool_3x3', 1), ('sep_conv_5x5', 0)], reduce_concat=[3, 4, 5, 6])

res_4_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('avg_pool_3x3', 4)], normal_concat=[3, 5, 6], reduce=[('avg_pool_3x3', 1), ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), ('dil_conv_3x3', 0), ('dil_conv_3x3', 3), ('avg_pool_3x3', 2), ('max_pool_3x3', 2), ('sep_conv_3x3', 0), ('dil_conv_3x3', 4), ('sep_conv_5x5', 0)], reduce_concat=[5, 6])

res_5_architecture = Genotype(normal=[('max_pool_3x3', 0), ('dil_conv_5x5', 1), ('avg_pool_3x3', 2), ('dil_conv_5x5', 2), ('avg_pool_3x3', 3), ('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1)], normal_concat=[4, 5, 6], reduce=[('dil_conv_5x5', 1), ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), ('sep_conv_3x3', 0), ('conv_7x1_1x7', 1), ('avg_pool_3x3', 3), ('dil_conv_3x3', 2), ('sep_conv_3x3', 0), ('max_pool_3x3', 0), ('sep_conv_5x5', 0)], reduce_concat=[4, 5, 6])

res_6_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('max_pool_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 3), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1)], normal_concat=[4, 5, 6], reduce=[('dil_conv_5x5', 1), ('sep_conv_3x3', 1), ('avg_pool_3x3', 2), ('sep_conv_3x3', 0), ('conv_7x1_1x7', 1), ('avg_pool_3x3', 3), ('dil_conv_3x3', 2), ('sep_conv_3x3', 0), ('max_pool_3x3', 0), ('sep_conv_5x5', 0)], reduce_concat=[4, 5, 6])

res_7_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 2), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('skip_connect', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1)], normal_concat=[3, 4, 5, 6], reduce=[('dil_conv_5x5', 1), ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), ('sep_conv_3x3', 0), ('conv_7x1_1x7', 0), ('avg_pool_3x3', 3), ('dil_conv_3x3', 2), ('sep_conv_3x3', 0), ('dil_conv_3x3', 5), ('sep_conv_5x5', 0)], reduce_concat=[4, 6])

res_8_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('dil_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1)], normal_concat=[3, 4, 5, 6], reduce=[('dil_conv_5x5', 1), ('sep_conv_3x3', 0), ('max_pool_3x3', 0), ('sep_conv_3x3', 0), ('conv_7x1_1x7', 0), ('avg_pool_3x3', 3), ('dil_conv_3x3', 2), ('sep_conv_3x3', 0), ('max_pool_3x3', 0), ('sep_conv_5x5', 0)], reduce_concat=[4, 5, 6])

res_9_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 0), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 1), ('dil_conv_5x5', 1)], normal_concat=[3, 4, 5, 6], reduce=[('dil_conv_5x5', 1), ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), ('sep_conv_3x3', 0), ('conv_7x1_1x7', 0), ('avg_pool_3x3', 3), ('dil_conv_3x3', 2), ('avg_pool_3x3', 0), ('max_pool_3x3', 0), ('sep_conv_5x5', 0)], reduce_concat=[4, 5, 6])

res_10_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1)], normal_concat=[3, 4, 5, 6], reduce=[('dil_conv_5x5', 1), ('dil_conv_3x3', 1), ('avg_pool_3x3', 2), ('sep_conv_3x3', 0), ('conv_7x1_1x7', 0), ('avg_pool_3x3', 3), ('dil_conv_3x3', 2), ('sep_conv_3x3', 0), ('max_pool_3x3', 0), ('sep_conv_5x5', 0)], reduce_concat=[4, 5, 6])

res_11_architecture = Genotype(normal=[('max_pool_3x3', 0), ('avg_pool_3x3', 0), ('avg_pool_3x3', 1), ('sep_conv_5x5', 2), ('max_pool_3x3', 1), ('sep_conv_3x3', 1), ('sep_conv_5x5', 0), ('dil_conv_3x3', 2), ('dil_conv_5x5', 2), ('dil_conv_5x5', 1)], normal_concat=[3, 4, 5, 6], reduce=[('dil_conv_5x5', 1), ('sep_conv_3x3', 1), ('avg_pool_3x3', 2), ('sep_conv_3x3', 0), ('conv_7x1_1x7', 1), ('avg_pool_3x3', 3), ('dil_conv_3x3', 2), ('sep_conv_3x3', 0), ('max_pool_3x3', 0), ('sep_conv_5x5', 0)], reduce_concat=[4, 5, 6])

# # 20230116 pareto front plot for evolutionary micro search archi 100 epoch 20




