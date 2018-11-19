import numpy as np
import mdtraj as md
import glob

class adptvSmp:
  """
  
  """
        def __init__(self):
                return
  
        def ftr_rmsd_dist(self):
                """
                
                """
                # favorite residues to compute distance(s)
                cont=[[149, 267]]
                # reference structure for calculating RMSD
                # numbering the outputs
                ref_2hyy=md.load('2HYY.pdb')
                count=0
                for file in glob.glob('stripedTrj/MD1-strTrj/2HYY*'):
                        t = md.load(file, top='2HYY.prmtop')
                        rmsds = md.rmsd(t, ref_2hyy, frame=0)
                        dist=md.compute_contacts(t, contacts=cont)
                        ftr=[[dist[0][i][0],rmsds[i]] for i in range(len(rmsds))]
                        np.save(str(count)+'.npy', ftr)
                        count=count+1
                return
        
    