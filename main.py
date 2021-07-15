from Tracker import *
import argparse
from polyroi import Shape, Point

confirm_box = False
draw_rectangle = False
box_x = 0
box_y = 0
box_w = 0
box_h = 0


#OpenCV callback function to get the area of the user selected vertebrate
def selectTarget(event, x, y, flags, param):
    global box_x, box_y, box_w, box_h, confirm_box, draw_rectangle

    if event == cv2.EVENT_MOUSEMOVE:
        if(draw_rectangle):
            box_w = x - box_x
            box_h = y - box_y

    elif event == cv2.EVENT_LBUTTONDOWN:
        draw_rectangle = True
        box_x = x
        box_y = y
        box_w = 0
        box_h = 0

    elif event == cv2.EVENT_LBUTTONUP:
        draw_rectangle = False
        if box_w < 0:
            box_x += box_w
        if box_h < 0:
            box_y += box_h
            box_h *= -1
        pt1 = (box_x, box_y)
        pt2 = (box_x + box_w, box_y + box_h)
        cv2.rectangle(param, pt1, pt2, (0, 255, 0), 2)
        confirm_box = True
    return


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--video", type=str, help="path to the video to be analyzed", required=True)
    parser.add_argument("-np", "--nb_particles", type=int, help="number of particles to be used for the tracking", required=False)
    parser.add_argument("-vs", "--vertebrate_speed", type=int, help="vertebrate speed (used to predict vertebrate motion)", required=False)
    parser.add_argument("-vr", "--vertebrate_rotation", type=int, help="vertebrate rotation (used to predict vertebrate motion)", required=False)
    parser.add_argument("-nv", "--nb_vertebrates", type=int, help="number of vertebrates to track", required=False)
    args = parser.parse_args()

    video = cv2.VideoCapture(args.video)

    ret, frame = video.read()
    
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    clahe = cv2.createCLAHE(clipLimit=40.0, tileGridSize=(8,8))
    frame[:,:,0] = clahe.apply(frame[:,:, 0])
    frame[:,:,1] = clahe.apply(frame[:,:, 1])
    frame[:,:,2] = clahe.apply(frame[:,:, 2])
    frame =  cv2.medianBlur(frame, 1)
    # frame = clahe.apply(frame[:,1])
    
    # frame =  cv2.medianBlur(frame, 5)
    # TODO add list of shapes
    d = Shape.get_roi(frame)

    
    # (image, target_shape, nb_particles, vertebrate_speed, vertebrate_rotation):
    # TODO add a list of trackers for each vertebrates
    tracker = Tracker(frame, d, args.nb_particles, args.vertebrate_speed, args.vertebrate_rotation)
    tracker.ParticlesInitilization()
    tracker.GetTargetHistogram()
    i = 0
    while 1:
        ret, frame = video.read()
        i += 1
        print(i)
        if not ret:
            break
        frame[:,:,0] = clahe.apply(frame[:,:, 0])
        frame[:,:,1] = clahe.apply(frame[:,:, 1])
        frame[:,:,2] = clahe.apply(frame[:,:, 2])
        frame =  cv2.medianBlur(frame, 1)
        
        tracker.ParticlesResampling()
        tracker.ParticlesMotionModel()
        tracker.ParticlesAppearanceModel(frame)
        tracker.UpdateParticlesWeight()
        tracker.UpdateTargetPosition()
        tracker.draw_particles(frame)
        tracker.draw_target(frame)
        # tracker.target_particle.particle.to_image(i, frame)

        cv2.imshow("Tracker", frame)
        if cv2.waitKey(30) == ord('q'):
            break

    video.release()
    cv2.destroyAllWindows()
    return 0


if __name__ == "__main__":
    main()
