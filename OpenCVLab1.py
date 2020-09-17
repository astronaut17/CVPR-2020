import cv2

cap = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'XVID')
vidout = cv2.VideoWriter('captured.avi', codec, 20, (640,480)) #Записуємо відео у файл
i=0
print("Saving video...(~12 seconds long)")
while(i<250):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or ret == False:
        break
    cv2.imshow('Your beautiful face here', frame) #Виводимо відео в першому вікні
    vidout.write(frame)
    i=i+1
vidout.release()
cap.release()

cap = cv2.VideoCapture('captured.avi') #Зчитуємо свіжезаписане відео
print("Playing edited video...")
while(True): 
    ret, frame = cap.read()
    if cv2.waitKey(30) & 0xFF == ord('q') or ret == False:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #Зберігаємо кадр у відтінках сірого
    image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR) #Перезаписуємо його в BGR щоб намалювати кольорові фігури
    cv2.rectangle(image,(300,300),(60,30),(255,0,0),3) #Малюємо синій прямокутник
    cv2.line(image,(450,150),(600,200),(0,0,255),5) #Малюємо червону лінію
    cv2.imshow('Your edited video', image) #Виводимо змінене відео в другому вікні
cap.release()
cv2.destroyAllWindows()