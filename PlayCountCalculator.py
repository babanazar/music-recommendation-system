import numpy as np
import h5py
from scipy import sparse

UAM_MATLAB_FILE = 'dataset/LFM-1b_LEs.mat'
STATISTICS_OUTPUT_FILE = 'UserSongPlayCounts.txt'

def read_UAM(m_file):
    mf = h5py.File(m_file, 'r')
    user_ids = np.array(mf.get('idx_users')).astype(np.int64)
    artist_ids = np.array(mf.get('idx_artists')).astype(np.int64)
    # Load UAM
    UAM = sparse.csr_matrix((mf['/LEs/']["data"],
                             mf['/LEs/']["ir"],
                             mf['/LEs/']["jc"])).transpose()    #.tocoo().transpose()
    # user and artist indices to access UAM
    UAM_user_idx = UAM.indices #UAM.row -> for COO matrix
    UAM_artist_idx = UAM.indptr #UAM.col -> for COO matrix
    return UAM, UAM_user_idx, UAM_artist_idx, user_ids, artist_ids


if __name__ == '__main__':
    # Read UAM
    UAM, UAM_user_idx, UAM_artist_idx, user_ids, artist_ids = read_UAM(UAM_MATLAB_FILE)
    print('Users: ', len(user_ids))
    print('Artists: ', len(artist_ids))
    print(UAM)