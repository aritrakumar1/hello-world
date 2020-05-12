from tkinter import *
#import bluetooth,os

port=14
a=[]
root_status=1
crt=[]

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

                                    #STARTING OF LIST MAKING

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def makelist():
    global root1,a,add_pro
    try:
        myfile=open("list.txt","r") #READ OLD ITEM FROM THE FILE
        x=myfile.read()
        a=eval(x)
        myfile.close()
    except:
        a=[]

    def add(): #ADDING ITEM TO THE LIST
        a.append(add_pro.get())

    def add_list():  #WRITE ITEM TO THE FILE
        global a,c
        myfile=open("list.txt","w")
        myfile.write(str(a))
        myfile.close()

    def des_list():     #FOR GO BACK TO 1ST WINDOW
        global root1
        root1.destroy()
        home()
    
    global root
    root.destroy()    #1ST PAGE IS CLOSED

    root1=Tk()          #START A NEW GUI FOR ADD PRODUCT 
    Label(root1,text="Add product").grid(row=0,column=0)
    add_pro=Entry(root1)
    add_pro.grid(row=0,column=1)
    
    Button(root1,text="Back",command=des_list).grid(row=1,column=3)
    Button(root1,text="Add",command=add).grid(row=1,column=2)
    Button(root1,text="save",command=add_list).grid(row=1,column=1)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

                                    #END OF MAKE LIST

                                    #STARTING OF SHOW SAVE LIST

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

    
def savelist():
    def bk_to_savelist():  #GO TO SAVE LIST PAGE FROM PRICE LIST PAGE
        global price_list
        price_list.destroy()
        savelist()
    def bk():               #GO BACK TO 1ST WINDOW
        global  root2
        root2.destroy()
        home()
        
    def ser_list():     #SEARCH ITEMS IN SERVER ACCORDING  TO THE LIST
        global price_list,root2,crt
        rcv_list=[]
        root2.destroy()
        price_list=Tk()

        #<<<<send my_list_str to server>>>>>>

        myfile=open("list.txt","r") #READ OLD ITEM FROM THE FILE
        my_list_str=myfile.read()
        my_list_arr=eval(my_list_str)
        myfile.close()


        
        for search_product in my_list_arr:

            #<<<<send search_product to server>>>>>
           
            client_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            addr='4c:bb:58:b7:64:4a' #ENTER MACK ADDRESS OF THE SERVEER
            client_sock.connect((addr,port))
            client_sock.send(search_product)
            client_sock.close()

                
            #<<<<<received details stored in rcv_pro>>>>>


#            server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#            server_sock.bind(("",port))
#            server_sock.listen(1)
#            client_sock,address=server_sock.accept()
#            #print "accepted connection from: ",addr
#            rcv=client_sock.recv(1024)
#            print rcv
#            rcv_list.append(eval(rcv))#ADD PRODUCTDETAILS TO THE RCV_LIST ARRAY
#            client_sock.close()
#            server_sock.close()



        
        #rcv_list=[['soap','40'],['oil','100']]
        Label(price_list,text="Product   |").grid(row=0,column=0)
        Label(price_list,text="  Price  ").grid(row=0,column=1)
        

        j=1
        for i in rcv_list:   #SHOW DETAILS OF LISTED ITEM FROM SERVER
            Label(price_list,text=str(j)+".  "+str(i[0])).grid(row=j,column=0)
            Label(price_list,text=str(i[1])).grid(row=j,column=1)
            Button(price_list,text="add to cart",command=crt.append(i)).grid(row=j,column=3)
            j=j+1

        Button(price_list,text="Back",command=bk_to_savelist).grid(row=j,column=2)


    global root2,root,root_status,crt
    
    if(root_status==0):
        root.destroy()  #DETROY 1ST PAGE
        root_status=1

    chk_lst=[]
    root2=Tk()
    try:
        myfile=open("list.txt","r")#READ ITEMS FROM FILE
        my_list_str=myfile.read()
        my_list_arr=eval(my_list_str)
        myfile.close()

        j=1

        for i in my_list_arr:   #SHOW THE SAVE ITEM IN DIFFERENT LEVELS
            Label(root2,text=str(j)+".  "+str(i)).grid(row=j,column=0)
            j=j+1
        Button(root2,text="Search availability",command=ser_list).grid(row=j,column=1)
        Button(root2,text="Back",command=bk).grid(row=j+1,column=1)
    except:
        Label(root2,text="EMPTY LIST",width=15).grid(row=0,column=0)
        Button(root2,text="Back",command=bk).grid(row=1,column=1)
        


#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

                                ##END OF SAVE LIST

                                ##STARTING OF SEARCHING OPERATION
    
 #||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
   
def search():
    def des_ser():          #GO BACK TO 1ST WINDOW
        global root_search
        root_search.destroy()
        home()
    def go_to():        #GO BACK TO SEARCH WINDOW

        global fnd_pro
        fnd_pro.destroy()
        search()
    def ser():      #SEARCHING FUNCTION IS CALLED

        global search_product,crt,rcv_pro
        

        #<<<<send search_product to server>>>>>

        search_product=get_pro.get()
        client_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        addr='4c:bb:58:b7:64:4a' #ENTER MACK ADDRESS OF THE SERVEER
        client_sock.connect((addr,port))
        client_sock.send(str(search_product))
        client_sock.close()

                
        #<<<<<received details stored in rcv_pro>>>>>


#        server_sock=bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#        server_sock.bind(("",port))
#        server_sock.listen(1)
#        client_sock,address=server_sock.accept()
#        print "accepted connection from: ",addr
#        rcv_pro=client_sock.recv(1024)
#        print rcv_pro
#        client_sock.close()
#        server_sock.close()
#        rcv_pro=eval(rcv_pro)


        #rcv_pro=['trimmer','2000','personal','electroics']                    
        root_search.destroy()   #FOR DESTROYNG SEARCH WINDOW

        global fnd_pro,rec_pro
        fnd_pro=Tk()    #A NEW TKINTER FOR SHOWING THE DETAILS OF SEARCH ITEM
        Label(fnd_pro,text="Product =>   ").grid(row=0,column=0)
        Label(fnd_pro,text="PRICE =>   ").grid(row=1,column=0)
        Label(fnd_pro,text="Position =>  ").grid(row=2,column=0)

        Label(fnd_pro,text=str(rcv_pro[0])).grid(row=0,column=1)
        Label(fnd_pro,text=str(rcv_pro[1])).grid(row=1,column=1)
        #Label(fnd_pro,text=str(rcv_pro[2])).grid(row=2,column=1)

        Button(fnd_pro,text="Add to cart",width =15,command=crt.append(rcv_pro)).grid(row=3,column=0)  #command=crt.append(rcv_pro),
        Button(fnd_pro,text="Similar",width =15).grid(row=4,column=0)
        Button(fnd_pro,text="Back",command=go_to).grid(row=5,column=1)


    global root,root_search,root_status,crt
    if(root_status==0):
        root.destroy()  #DETROY 1ST PAGE
        root_status=1

    root_search=Tk()        #A NEW TIKINTER FOR SEARCH
    Button(root_search,text="Cart",command=cart).grid(row=0,column=2)

    #<<<<<<<IMAGE PROCESSING>>>>>>

    Label(root_search,text="Enter product code").grid(row=1,column=0)
    Button(root_search,text="Search",command=ser).grid(row=2,column=1)
    Button(root_search,text="Back",command=des_ser).grid(row=2,column=2)
    global search_product    
    get_pro=Entry(root_search)
    get_pro.grid(row=1,column=1)
    
##    Label(root2,text="TEXT BOX").grid(row=0,column=0)
##    textbox_v=Text(root2)
##    textbox_v.grid(row=1,column=0)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

                                                    ##END OF SEARCH OPERATION

                                                    ##STARTING OF SCAN
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||



def scan():

    #<<<<<<<<<<<<<<<<image processing>>>>>>>>>>>>>>>>
    root4=Tk()
    
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

                                                            ##END OF SCAN

                                                            ##STARTING OF OFFER

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def offer():
    def bk_frm_ofr(): #BACK TO HOME PAGE
        global root_offer
        root_offer.destroy()
        home()
    def bk_to_ofr():        #BACK TO 1ST OFFER PAGE
        global root_ofr
        root_ofr.destroy()
        offer()

    def ofr():          #CALL SERVER TOO CHECK DEALS
        global root_ofr,root_offer,crt
        root_offer.destroy()
        root_ofr=Tk()
        #<<<<received string from server,converted to array as offr >>>>>
        Label(root_ofr,text="Product name    |").grid(row=0,column=0)
        Label(root_ofr,text="     Price").grid(row=0,column=2)
        j=1
##        for i in offr:
##            Label(root_offer,text=str(j)+". "+i[0]).grid(row=j,column=0)
##            Label(root_offer,text=i[1]).grid(row=j,column=2)
##            Button(root_offer,text="add to cart",command=crt.append(i)).grid(row=j,column=3)  #SEND PRODUCT NAME IN CART FUNCCTION
##            j=j+1
    
        Button(root_ofr,text="Back",command=bk_to_ofr).grid(row=j,column=2)

    global root,root_offer,root_status,crt
    if(root_status==0):
        root.destroy()  #DETROY 1ST PAGE
        root_status=1

    root_offer=Tk()
    Button(root_offer,text="Today's deal",command=ofr,width=15).grid(row=1,column=0)  #SEND 1 TO SERVER FOR TODAY'S DEAL
    #Button(root_offer,text="This week special",width=15).grid(row=2,column=0)
    Button(root_offer,text="Upcomming deal",command=ofr,width=15).grid(row=2,column=0) #SEND 2 TO SERVER FOR UPCOOMMING DEAL
    Button(root_offer,text="Back",command=bk_frm_ofr).grid(row=3,column=0)

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

                                        ##END OF OFFER

                                        ##STARTING OF CART

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def cart():
    global crt
    root_crt=Tk()
    Label(root_crt,text="Product   |").grid(row=0,column=0)
    Label(root_crt,text="   Price").grid(row=0,column=1)
        
    total=0
    j=1
    for i in crt:
        Label(root_crt,text=i[0]).grid(row=j,column=0)
        Label(root_crt,text=i[1]).grid(row=j,column=1)
        total=total+int(i[1])
        j=j+1

    Label(root_crt,text="Total").grid(row=j,column=0)
    Label(root_crt,text=str(total)).grid(row=j,column=1)
    Button(root_crt,text="Check out").grid(row=j+1,column=0) #command not ready       

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

                                        ##END OF CART

                                        ##STARTING OF HOME PAGE

#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


def home():
    global root,root1,root2,root_search,find_pro,root_status
##    root1.destroy()
##    root2.destroy()
##    root_search.destroy()
##    find_pro.destroy()

    
    root=Tk()
    root_status=0

    Button(root,text="Make a List         =>",command=makelist).grid(row=0,column=0)
    Button(root,text="Check Saved List=>",command=savelist).grid(row=1,column=0)
    Button(root,text="Search                 =>",command=search).grid(row=2,column=0)
    Button(root,text="Scan                    =>",command=scan).grid(row=3,column=0)
    Button(root,text="Offer                    =>",command=offer).grid(row=4,column=0)
    Button(root,text="Cart                      =>",command=cart).grid(row=5,column=0)

    root.mainloop()


home()
#end of code