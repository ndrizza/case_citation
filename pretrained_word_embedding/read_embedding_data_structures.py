"""
This code just shows how to read the stored files.
"""

import pickle
import bcolz
import torch

# read vocabulary
vocabulary = pickle.load(open('glove.6B/vocabulary.pkl', 'rb'))
# read word to index mapping
word2idx = pickle.load(open('glove.6B/word2idx.pkl', 'rb'))
# read index to embedding vector mapping
idx2vec = bcolz.open('glove.6B/idx2vec.dat')[:]
# read word embedding weight matrix
weight_matrix = torch.load(open('glove.6B/weight_matrix.pt', 'rb'))

# create full glove mapping
glove = {w: idx2vec[word2idx[w]] for w in vocabulary}

print(glove['the'])
# assert that it is
# 0.418 0.24968 -0.41242 0.1217 0.34527 -0.044457 -0.49688 -0.17862 -0.00066023 -0.6566 0.27843 -0.14767 -0.55677 0.14658 -0.0095095 0.011658 0.10204 -0.12792 -0.8443 -0.12181 -0.016801 -0.33279 -0.1552 -0.23131 -0.19181 -1.8823 -0.76746 0.099051 -0.42125 -0.19526 4.0071 -0.18594 -0.52287 -0.31681 0.00059213 0.0074449 0.17778 -0.15897 0.012041 -0.054223 -0.29871 -0.15749 -0.34758 -0.045637 -0.44251 0.18785 0.0027849 -0.18411 -0.11514 -0.78581
print(weight_matrix[1])