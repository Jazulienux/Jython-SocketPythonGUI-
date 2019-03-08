import socket
import sys
from javax.swing import *
from java.lang import *
import rospy
from std_msgs.msg import String

if __name__ == '__main__':
    
    
    frame = JFrame("Robsonema Team")
    frame.setSize(200, 150)
    frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE)

    sockConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockConn.connect(("192.168.245.63", 28097))
    
    while True:
        try:
            data = sockConn.recv(1024)
            print(data)
            # Create Panel and add swing components and show it.
            if data == "W":
                ket = data + " ==> Pemilihan Tim Cyan / Magenta"
            elif data == "s":
                ket = data + " ==> Start Team Cyan / Magenta"
            elif data == "S":
                ket = data + " ==> Stop Team Cyan / Magenta"
            elif data == "L":
                ket = data + " ==> Park Team Cyan / Magenta"
            elif data == "N":
                ket = data + " ==> DroppedBall Team Cyan / Magenta"
            elif data == "h":
                ket = data + " ==> Half Time Team Cyan / Magenta"
                data = None
            elif data == "e":
                ket = data + " ==> End Part Team Cyan / Magenta"
                data = None
            elif data == "e":
                ket = data + " ==> Reset Game"
                data = None
                
            elif data == "K":
                ket = data + " ==> KickOf Team Cyan"
            elif data == "F":
                ket = data + " ==> FreeCick Team Cyan"
            elif data == "G":
                ket = data + " ==> GoalKick Team Cyan"
            elif data == "T":
                ket = data + " ==> ThrowIn Team Cyan"
            elif data == "C":
                ket = data + " ==> CornerKick Team Cyan"
            elif data == "P":
                ket = data + " ==> PenaltyKick Team Cyan"
            elif data == "O":
                ket = data + " ==> Repair Team Cyan"
            elif data == "A":
                ket = data + " ==> Goal Team Cyan"
            elif(data=="Y"):
                ket = data + " ==> Yellow For Cyan"
            elif(data=="R"):
                ket = data + " ==> Red For Cyan"
            
            elif(data=="k"):
                ket = data + " ==> KickOf Team Magenta"
            elif(data=="f"):
                ket = data + " ==> FreeCick Team Magenta"
            elif(data=="g"):
                ket = data + " ==> GoalKick Team Magenta"
            elif(data=="t"):
                ket = data + " ==> ThrowIn Team Magenta"
            elif(data=="c"):
                ket = data + " ==> CornerKick Team Magenta"
            elif(data=="p"):
                ket = data + " ==> PenaltyKick Team Magenta"
            elif(data=="o"):
                ket = data + " ==> Repair Team Magenta"
            elif(data=="a"):
                ket = data + " ==> Goal Team Magenta"
            elif(data=="y"):
                ket = data + " ==> Yellow For Magenta"
            elif(data=="r"):
                ket = data + " ==> Red For Magenta"

            
            pnl = JPanel()
            frame.add(pnl)
#            setIp = JTextField("Set IP Address Referee Box !!",30)
#            pnl.add(setIp)
#            btn = JButton("Connect")   
#            pnl.add(btn)
            parsing = JTextField(ket,30)
            pnl.add(parsing) 
    
            frame.pack()
            frame.setVisible(True)
            
            pub = rospy.Publisher('SocketData', String, queue_size=10)
            rospy.init_node('/SocketData', anonymous=True)
            rate = rospy.Rate(10) # 10hz
            while not rospy.is_shutdown():
                send = data
                rospy.loginfo(send)
                send = JTextField(send + " ==> Send On Robot",30)
                pnl.add(send)
                pub.publish(send)
                rate.sleep()

        except:
            if data is None:
                sockConn.close()
                sys.exit(1)
                break
                

