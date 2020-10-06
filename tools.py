import numpy as np
import  open3d as o3d

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

def pcl_bounds(pcl):
    '''
    Find bounds of point clouds in open3d

    Parameters:
    -----------
    pcl: open 3d point cloud object for which boundaries are being found

    Returns:
    --------
    pcl_bounds: np array of min and max xyz coordinates in the following format
        [[xmin,ymin,zmin],
        [xmax,ymax,zmax]]

    '''

    bound_box=pcl.get_axis_aligned_bounding_box()

    xmin=bound_box.get_min_bound()[0]
    xmax=bound_box.get_max_bound()[0]
    ymin=bound_box.get_min_bound()[1]
    ymax=bound_box.get_max_bound()[1]
    zmin=bound_box.get_min_bound()[2]
    zmax=bound_box.get_max_bound()[2]

    pcl_bounds=np.array([[xmin,ymin,zmin],
                        [xmax,ymax,zmax]])

    return pcl_bounds

def crop_box(xmin,xmax,ymin,ymax,zmin,zmax):
    '''
    Create box used to crop point clouds in open3d.

    Use: pcl_crop=pcl.crop(crop_box)
    
    Parameters:
    -----------
    xmin: 
    xmax:
    ymin:
    ymax:
    zmin:
    zmax:

    Returns:
    --------
    crop_box: open3D Oriented Bounding Box

    To Do
    -----
    [ ] Set up default values
    [ ] Incorporate with pcl_bounds
    '''
    
    # set up np array
    crop_pts=np.array([[xmin,ymin,zmin],
              [xmax,ymin,zmin],
              [xmin,ymax,zmin],
              [xmin,ymin,zmax],
              [xmax,ymax,zmax],
              [xmin,ymax,zmax],
              [xmax,ymin,zmax],
              [xmax,ymax,zmin]])
    
    # convert to o3d format
    crop_pts=o3d.utility.Vector3dVector(crop_pts)

    #create OBB for crop object
    crop_box=o3d.geometry.OrientedBoundingBox.create_from_points(crop_pts)

    # print bounds to check
    print('Min Bounds:')
    print(crop_box.get_min_bound())
    print('-----------------------')
    print('Max Bounds:')
    print(crop_box.get_max_bound())
    
    return crop_box