<img src="https://www.presse.tu-clausthal.de/fileadmin/Presse/images/Corporate_Design/Logo/Logo_TUC_en_CMYK.jpg" width="300">

# rpi-camera-af
Auto focus camera using Raspberry Pi, lens and a servo motor

Abstract
This project aimed to design and develop a modular camera platform using a Raspberry Pi,
integrating various components such as a camera sensor, a wide lens, an FS90R servo
motor, and 3D-printed gears. The primary objective was to create an autofocus mechanism
that dynamically adjusts focus by calculating the Laplacian variance of live frame previews
to achieve optimal sharpness. The methodology involved assembling the hardware
components, programming the Raspberry Pi to control the servo motor based on image
sharpness metrics, and enabling real-time focus adjustments. Initial tests demonstrated
that while the system could effectively identify and adjust to changes in frame sharpness,
limitations related to the precision of the lens's focal point, the quality of the sensor, and the
accuracy of the servo motor control were identified. These factors affected the overall
efficacy of the autofocus system. The project concluded that while the prototype showed
potential, enhancements in hardware precision and control algorithms are necessary for
practical applications. Future work will focus on refining these elements to improve system
reliability and performance.

Materials and Methods
In this project, we used several hardware components and software tools to build our
modular camera system. The core of our setup was the Raspberry Pi 4, a powerful model
with sufficient processing capabilities for image handling and device control. This
microcontroller was chosen for its robust support and ability to interface with various
peripherals via its GPIO (General Purpose Input/Output) pins. Alongside the Raspberry Pi,
we employed a camera sensor designed to connect to the Raspberry Pi via the 2-lane MIPI
CSI camera port. This setup allowed us to capture high-quality images directly processed by
the Raspberry Pi.
For the movement and focusing mechanism, we used an FS90R servo motor. This compact
and lightweight motor was connected to the Raspberry Pi’s GPIO pins, which provided the
control signals required to adjust the motor’s position. The servo motor’s role was critical in
adjusting the lens for optimal focus, driven by feedback from the image processing software.
Additionally, we utilized two 3D-printed gears; one gear was mounted on the camera lens
and the other on the servo motor. These gears were strategically positioned to mesh
perfectly, enabling the motor’s rotations to adjust the lens focus accurately.
On the software side, we leveraged several libraries to facilitate our camera system’s
functionality. We used OpenCV (CV2) for real-time image processing, which included
calculating the Laplacian variance to determine image sharpness. For camera control, we
used the PiCamera 2 library, which is specifically designed for interfacing with the Raspberry
Pi’s camera module, allowing us to capture and manipulate images directly. The RPi.GPIO
library was employed to manage the GPIO pins for servo motor control, providing the
necessary instructions based on the image processing results.
The assembly process involved carefully integrating these components. We started by
connecting the camera sensor to the Raspberry Pi via the MIPI CSI port and setting up the
servo motor via the GPIO pins. Next, the gears were attached—one on the lens and the other
on the servo motor. We positioned the motor close enough to the lens so that the gears could
engage correctly to transfer motion from the motor to the lens. This setup ensured that when
the motor activated, the lens would rotate to adjust focus based on our software analysis.
This methodical assembly ensured all parts worked in harmony, allowing for precise control
and optimal image clarity.

System Design and Implementation
Our modular camera system features a well-coordinated assembly of hardware and software,
designed to automate focusing through a manual lens using a Raspberry Pi 4 as the central controller.
For the hardware, the core component is the Raspberry Pi 4, interfacing with a camera sensor
connected via the 2-lane MIPI CSI camera port for high-quality image capture. The autofocus is
managed by an FS90R servo motor, which adjusts the lens position based on focus requirements.
This motor is controlled through the Raspberry Pi’s GPIO pins. The manual focus adjustment is
accomplished using two 3D-printed gears: one attached to the lens and the other to the servo motor.
These gears are designed to engage with each other, allowing the servo motor's movements to adjust
the lens focus directly.
On the software side, our system utilizes several Python libraries to handle image processing and
device control. We use cv2 for image processing tasks, such as calculating image sharpness, and
Picamera2 for handling camera operations. The RPi.GPIO library is crucial for controlling the GPIO
pins that drive the servo motor. To manage these processes simultaneously, we employ Python’s
threading module, allowing us to maintain a live view from the camera while adjusting focus in real-
time.
The provided Python script illustrates the integration and functionality of these components. The
FrameVarianceMonitor class is designed to track the sharpness of consecutive images, storing the
variance values to determine when maximum focus is achieved. Functions such as rightmove() and
leftmove() control the motor’s direction to adjust the lens, using the pwm.ChangeDutyCycle method
to send the appropriate signals to the servo. The main function, moarso(), orchestrates the autofocus
process by comparing sharpness values from consecutive frames and deciding the direction of
motor movement based on whether the image sharpness is improving.
Finally, the integration of the servo motor with the lens via 3D-printed gears is a key aspect of our
system’s design, ensuring that each adjustment in motor output translates directly into lens
movement. This setup is meticulously managed by our Python scripts, which handle the complex
task of focusing by continuously analyzing image quality and adjusting the lens position accordingly.
This ensures our camera system not only captures clear images but also operates efficiently,
maintaining a balance between performance and simplicity in its operation. The entire system is
designed to be robust yet flexible, allowing for real-time adjustments and optimizations based on
immediate feedback from the image processing algorithms.
To enhance the focusing capabilities of our modular camera system, we implemented various
innovative methods, each tailored to optimize image clarity under different scenarios. These
methods are designed to make full use of the programmable features of the Raspberry Pi and the
mechanical setup we developed. Here’s a breakdown of these methods:
Page 7 of 191. Heatmap-Based Focusing: This method involves analyzing the 'heat' distribution in a frame
to determine areas of highest activity or change, which often correspond to important focal
points in an image. By generating a heatmap of each frame, the system identifies the 'hottest'
part, which is likely to need sharper focus. This technique is particularly useful in dynamic
environments where significant parts of the scene might change rapidly, such as in wildlife
photography or in security applications.
2. Section-Based Focus: This user-driven method allows for selective focusing based on the
user's input via a mouse click. When a section of the image is selected, the system focuses
specifically on that area, adjusting the lens accordingly. This method is especially beneficial
for controlled scenarios like macro photography or when precise depth of field control is
desired. It provides the user with the flexibility to prioritize specific parts of the scene over
others.
3. Comprehensive Frame Focusing: We explored two strategies to achieve optimal focus
across the entire frame. The first strategy sets a threshold for the number of attempts the
system will make to find the frame with the highest variance—indicative of sharp focus—
before stopping and capturing the image. The second strategy involves rotating the lens in
both directions multiple times to determine the optimum lens position. This method ensures
that the focus is refined by considering multiple positions and selecting the one that
consistently provides the best clarity.
4.One of the main challenges we encountered was the inability to achieve micro-adjustments with the
motor and lens system, as the gears and motor setup did not allow for minute, millimeter-level
changes. This limitation made it difficult to achieve extremely precise focus, particularly in scenarios
requiring a very shallow depth of field or when dealing with micro-scale subjects. However, through
iterative testing and refinement, we developed practical algorithms that approximate the best
possible focus within the mechanical constraints. Once the optimal focus position is found, the
system maintains that position until a significant change in the scene is detected—such as
movements or lighting changes—which triggers a re-evaluation of the focus to ensure continuous
clarity.
These methods collectively enhance the usability and functionality of our camera system, providing
both automated and user-controllable options to achieve the desired focus, and adaptively
responding to changes in the environment to maintain image quality.


System Design and Implementation
Our modular camera system features a well-coordinated assembly of hardware and software,
designed to automate focusing through a manual lens using a Raspberry Pi 4 as the central controller.
For the hardware, the core component is the Raspberry Pi 4, interfacing with a camera sensor
connected via the 2-lane MIPI CSI camera port for high-quality image capture. The autofocus is
managed by an FS90R servo motor, which adjusts the lens position based on focus requirements.
This motor is controlled through the Raspberry Pi’s GPIO pins. The manual focus adjustment is
accomplished using two 3D-printed gears: one attached to the lens and the other to the servo motor.
These gears are designed to engage with each other, allowing the servo motor's movements to adjust
the lens focus directly.
On the software side, our system utilizes several Python libraries to handle image processing and
device control. We use cv2 for image processing tasks, such as calculating image sharpness, and
Picamera2 for handling camera operations. The RPi.GPIO library is crucial for controlling the GPIO
pins that drive the servo motor. To manage these processes simultaneously, we employ Python’s
threading module, allowing us to maintain a live view from the camera while adjusting focus in real-
time.
The provided Python script illustrates the integration and functionality of these components. The
FrameVarianceMonitor class is designed to track the sharpness of consecutive images, storing the
variance values to determine when maximum focus is achieved. Functions such as rightmove() and
leftmove() control the motor’s direction to adjust the lens, using the pwm.ChangeDutyCycle method
to send the appropriate signals to the servo. The main function, moarso(), orchestrates the autofocus
process by comparing sharpness values from consecutive frames and deciding the direction of
motor movement based on whether the image sharpness is improving.
Finally, the integration of the servo motor with the lens via 3D-printed gears is a key aspect of our
system’s design, ensuring that each adjustment in motor output translates directly into lens
movement. This setup is meticulously managed by our Python scripts, which handle the complex
task of focusing by continuously analyzing image quality and adjusting the lens position accordingly.
This ensures our camera system not only captures clear images but also operates efficiently,
maintaining a balance between performance and simplicity in its operation. The entire system is
designed to be robust yet flexible, allowing for real-time adjustments and optimizations based on
immediate feedback from the image processing algorithms.
To enhance the focusing capabilities of our modular camera system, we implemented various
innovative methods, each tailored to optimize image clarity under different scenarios. These
methods are designed to make full use of the programmable features of the Raspberry Pi and the
mechanical setup we developed. Here’s a breakdown of these methods:
1. Heatmap-Based Focusing: This method involves analyzing the 'heat' distribution in a frame
to determine areas of highest activity or change, which often correspond to important focal
points in an image. By generating a heatmap of each frame, the system identifies the 'hottest'
part, which is likely to need sharper focus. This technique is particularly useful in dynamic
environments where significant parts of the scene might change rapidly, such as in wildlife
photography or in security applications.
2. Section-Based Focus: This user-driven method allows for selective focusing based on the
user's input via a mouse click. When a section of the image is selected, the system focuses
specifically on that area, adjusting the lens accordingly. This method is especially beneficial
for controlled scenarios like macro photography or when precise depth of field control is
desired. It provides the user with the flexibility to prioritize specific parts of the scene over
others.
3. Comprehensive Frame Focusing: We explored two strategies to achieve optimal focus
across the entire frame. The first strategy sets a threshold for the number of attempts the
system will make to find the frame with the highest variance—indicative of sharp focus—
before stopping and capturing the image. The second strategy involves rotating the lens in
both directions multiple times to determine the optimum lens position. This method ensures
that the focus is refined by considering multiple positions and selecting the one that
consistently provides the best clarity.
4.One of the main challenges we encountered was the inability to achieve micro-adjustments with the
motor and lens system, as the gears and motor setup did not allow for minute, millimeter-level
changes. This limitation made it difficult to achieve extremely precise focus, particularly in scenarios
requiring a very shallow depth of field or when dealing with micro-scale subjects. However, through
iterative testing and refinement, we developed practical algorithms that approximate the best
possible focus within the mechanical constraints. Once the optimal focus position is found, the
system maintains that position until a significant change in the scene is detected—such as
movements or lighting changes—which triggers a re-evaluation of the focus to ensure continuous
clarity.
These methods collectively enhance the usability and functionality of our camera system, providing
both automated and user-controllable options to achieve the desired focus, and adaptively
responding to changes in the environment to maintain image quality.


