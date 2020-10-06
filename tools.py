import numpy as np

# write a function for creating Transform matrix
def transform(theta=0,xtrans=0,ytrans=0,ztrans=0):
    '''
    Sets up transformation  matrix to be applied to point cloud in open3D
    
    Parameters:
    -----------
    theta: angle to be rotated [degrees]. Default 0.
    xtrans: translation in x [units unsure]. Default 0.
    ytrans: translation in y [units unsure]. Default 0.
    ztrans: translation in z [units unsure]. Default 0.
    
    Returns:
    --------
    T: The desired transformation matrix

    '''
    
    # Initialize transformation matrix
    T=np.eye(4)
    
    if theta != 0:
        # Convert angle to radians
        theta=np.radians(theta)

        # Apply rotations
        T[0,0]=np.cos(theta)
        T[1,1]=np.cos(theta)
        T[0,1]=-np.sin(theta)
        T[1,0]=np.sin(theta)
    
    # Apply translations
    T[0,3]=xtrans #tx
    T[1,3]=ytrans #ty
    T[2,3]=ztrans #tz
    
    return T