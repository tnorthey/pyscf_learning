'''
basis set energy convergence for CCSD(T)
'''

import pyscf

basis_sets = ['ccpvdz', 'ccpvtz', 'ccpvqz']

for basis in basis_sets:

    print(basis)
    
    mol = pyscf.M(
        atom = 'H 0 0 0; F 0 0 1.1',
        basis = basis)
    
    mf = mol.RHF().run()
    mycc = mf.CCSD().run()
    et = mycc.ccsd_t()
    print('CCSD(T) correlation energy', mycc.e_corr + et)

