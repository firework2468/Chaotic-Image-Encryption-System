# Chaotic-Image-Encryption-System

# Introduction
This is a chaotic image encryption system based on DNA coding for meeting user needs for image encryption and decryption. The system includes client and management side. The client provides users with image management, membership management and other operations, and the management terminal provides administrators with user management, news management, image management, usage statistics and other operations. This system adopts the development framework of Spring Boot + Vue, which maximizes the satisfaction of the basic needs of users and administrators using this system.
# Alogorithm
This system adopts a chaotic image encryption algorithm based on DNA coding and uses Python language to realize the processing of digital images. The algorithm processes the image according to the three color channels of RGB, uses the pixel information of the plaintext image as the initial value, and uses Logistic mapping to iteratively generate pseudo-random sequences; then according to the four sets of chaotic sequences generated by the Chen hyperchaotic system, it uses DNA coding rules and operations The rules perform block encryption and calculation operations on the plaintext image and the pseudo-random sequence; finally, all sub-blocks are merged and scrambled to obtain the ciphertext image. At the same time, the system uses numerical analysis to analyze various numerical indicators of the ciphertext image. The security of the encryption algorithm was tested by using common attack methods in cryptography. The experimental results show that the digital image encryption algorithm implemented by this system can resist common attack methods and also meet the verification of various values.