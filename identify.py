import cv2
import os
import numpy as np
import tkinter as tk
import tkinter.font as font
from tkinter import messagebox, simpledialog

def collect_data():
    # Create input dialog window
    input_window = tk.Toplevel()
    input_window.title("Add New Member")
    input_window.geometry("300x150")
    
    # Name input
    tk.Label(input_window, text="Name:").pack(pady=5)
    name_entry = tk.Entry(input_window, width=25)
    name_entry.pack()
    
    # ID input
    tk.Label(input_window, text="ID:").pack(pady=5)
    id_entry = tk.Entry(input_window, width=25)
    id_entry.pack()
    
    # Submit button
    def on_submit():
        name = name_entry.get().strip()
        user_id = id_entry.get().strip()
        
        if not name:
            messagebox.showerror("Error", "Please enter a name")
            return
        if not user_id.isdigit():
            messagebox.showerror("Error", "ID must be a number")
            return
            
        input_window.destroy()
        start_data_collection(name, user_id)
        
    submit_btn = tk.Button(input_window, text="Start Collection", command=on_submit)
    submit_btn.pack(pady=10)

def start_data_collection(name, user_id):
    # Create 'persons' directory if missing
    os.makedirs("persons", exist_ok=True)

    cap = cv2.VideoCapture(0)
    cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    count = 0
    while count < 300:  # Collect 300 samples
        ret, frame = cap.read()
        if not ret:
            continue
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, 1.4, 1)

        for (x, y, w, h) in faces:
            roi = gray[y:y+h, x:x+w]
            filename = f"persons/{name}-{count}-{user_id}.jpg"
            cv2.imwrite(filename, roi)
            count += 1

            # Show preview of face being captured
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            cv2.putText(frame, f"Samples: {count}/300", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        cv2.imshow("Collecting Face Data", frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    train()

def train():
    print("Training initiated...")
    dataset = "persons"
    paths = [os.path.join(dataset, f) for f in os.listdir(dataset)]

    faces = []
    ids = []

    for path in paths:
        try:
            # Parse filename safely
            filename = os.path.basename(path)
            parts = filename.split('-')
            if len(parts) < 3:
                print(f"Skipping invalid file: {filename}")
                continue

            user_id = int(parts[2].split('.')[0])
            img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                print(f"Failed to read image: {path}")
                continue

            faces.append(img)
            ids.append(user_id)
        except Exception as e:
            print(f"Error processing {path}: {e}")
            continue

    if len(faces) == 0:
        print("Error: No valid training data found.")
        return

    # Train and save the model
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.train(faces, np.array(ids))
    recognizer.save("model.yml")
    print("Model saved as model.yml")

def identify():
	if not os.path.exists("model.yml"):
		print("Error: Model not found. Train first.")
		return

	recognizer = cv2.face.LBPHFaceRecognizer_create()
	recognizer.read("model.yml")  # Load the model
	cap = cv2.VideoCapture(0)
	filename = "haarcascade_frontalface_default.xml"

	paths = [os.path.join("persons", im) for im in os.listdir("persons")]
	labelslist = {}
	for path in paths:
		labelslist[path.split('/')[-1].split('-')[2].split('.')[0]] = path.split('/')[-1].split('-')[0]

	print(labelslist)
	recog = cv2.face.LBPHFaceRecognizer_create()

	recog.read('model.yml')

	cascade = cv2.CascadeClassifier(filename)

	while True:
		_, frm = cap.read()

		gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY)

		faces = cascade.detectMultiScale(gray, 1.3, 2)

		for x,y,w,h in faces:
			cv2.rectangle(frm, (x,y), (x+w, y+h), (0,255,0), 2)
			roi = gray[y:y+h, x:x+w]

			label = recog.predict(roi)

			if label[1] < 100:
				cv2.putText(frm, f"{labelslist[str(label[0])]} + {int(label[1])}", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
			else:
				cv2.putText(frm, "unkown", (x,y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

		cv2.imshow("identify", frm)

		if cv2.waitKey(1) == 27:
			cv2.destroyAllWindows()
			cap.release()
			break

def maincall():


	root = tk.Tk()

	root.geometry("480x100")
	root.title("identify")

	label = tk.Label(root, text="Select below buttons ")
	label.grid(row=0, columnspan=2)
	label_font = font.Font(size=35, weight='bold',family='Helvetica')
	label['font'] = label_font

	btn_font = font.Font(size=25)

	button1 = tk.Button(root, text="Add Member ", command=collect_data, height=2, width=20)
	button1.grid(row=1, column=0, pady=(10,10), padx=(5,5))
	button1['font'] = btn_font

	button2 = tk.Button(root, text="Start with known ", command=identify, height=2, width=20)
	button2.grid(row=1, column=1,pady=(10,10), padx=(5,5))
	button2['font'] = btn_font
	root.mainloop()

	return


