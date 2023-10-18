'''
CCSD 2RDM and save to HDF5 format
'''

import tempfile
import h5py
import pyscf
from pyscf import lib

#basis_sets = ['ccpvdz', 'ccpvtz', 'ccpvqz']
    
mol = pyscf.M(
    atom = 'H 0 0 0; F 0 0 1.1',
    basis = 'ccpvdz')

mf = mol.RHF().run()
mycc = mf.CCSD().run()
et = mycc.ccsd_t()
print('CCSD(T) correlation energy', mycc.e_corr + et)
rdm2 = mycc.make_rdm2()
#print(rdm2)
lib.chkfile.save('rdm2.chk','rdm2',rdm2)
f = h5py.File('rdm2.chk', 'r')
print(f.keys())
print(f['rdm2'])


# make_rdm2(t1=None, t2=None, l1=None, l2=None, ao_repr=False, with_frozen=True, with_dm1=True)[source]¶
# 
#     2-particle density matrix in MO space. The density matrix is stored as
# 
#     dm2[p,r,q,s] = <p^+ q^+ s r>

