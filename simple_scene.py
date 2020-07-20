import os
import pybullet as pb

if __name__ == "__main__":
    
    uid = pb.connect(pb.GUI_SERVER)
    pb.resetSimulation()


    robot = pb.loadURDF(os.path.dirname(os.path.abspath(
        __file__)) + "/models/panda_arm.urdf", useFixedBase=True)
    ## for controlling and monitoring robots in pybullet, use motor controlling, joint info, link info
    # API from pybullet documentation. see usages in https://github.com/justagist/bullet_panda


    ## set objects as required in scene
    # instantiate table object, fix base, scale it as required, set its base position and orientation
    table = pb.loadURDF(os.path.dirname(os.path.abspath(
        __file__)) + "/models/table.urdf", useFixedBase=True, globalScaling=0.5)
    pb.resetBasePositionAndOrientation(
        table, [0.6, 0., 0.3], [0, 0, -0.707, 0.707]) # set table pose in world

    cylinder = pb.loadURDF(os.path.dirname(os.path.abspath(
        __file__)) + "/models/cylinder.urdf", useFixedBase=False, globalScaling=0.2)
    pb.resetBasePositionAndOrientation(
        cylinder, [0.6, 0., 0.5], [0, 0, -0.707, 0.707])  # set table pose in world

    pb.setGravity(0.0, 0.0, -9.8) # set gravity (x,y,z), if gravity is disabled, cylinder will float

    ## the next two lines run the simulation continuously in separate thread. If you want to 
    # step the simulation yourself comment out the next two lines and call pb.stepSimulation() 
    # when you need
    pb.setRealTimeSimulation(1)
    pb.setTimeStep(0.01)

    ## set up camera
    viewMatrix = pb.computeViewMatrix(
        cameraEyePosition=[0, 0, 3],
        cameraTargetPosition=[0, 0, 0],
        cameraUpVector=[0, 1, 0])

    projectionMatrix = pb.computeProjectionMatrixFOV(
        fov=45.0,
        aspect=1.0,
        nearVal=0.1,
        farVal=3.1)


    ## run simulation continuously
    while True:
        # pb.stepSimulation()

        ## get image from camera
        width, height, rgbImg, depthImg, segImg = pb.getCameraImage(
            width=224,
            height=224,
            viewMatrix=viewMatrix,
            projectionMatrix=projectionMatrix)

        continue
    
