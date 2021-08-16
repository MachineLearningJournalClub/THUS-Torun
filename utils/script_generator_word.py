import os

path='corpus2' 
bertpath='/home/wsojka00/Desktop/latin_bert' 


output='pickle_word'

if not os.path.exists(output):
  os.mkdir(output)

scriptfile = open('script.sh', 'w')

i=1

for a,b,c in os.walk(path):
	for txt in c:

		print("echo ' ",i,' su ',len(os.listdir(path))," ' ",file = scriptfile)
	
		outfile=os.path.splitext(txt)[0]
	
		#print('python3 gen_file_word.py --bertPath '+ bertpath +' --tokenizerPath '+ bertpath+ '/latin.subword.encoder -f '+ path +'/'+ b +'/' + txt +' -o  '+'/'+output+'/' +outfile , file = scriptfile )
		
		print('python3 gen_file_word.py --bertPath '+ bertpath +' --tokenizerPath '+ bertpath+ '/latin.subword.encoder -f  ./'+ path +'/' + txt +' -o  '+'./'+output+'/' +outfile , file = scriptfile )
		
		
		#print('python3  gen_file_word.py --bertPath '+ bertpath +' --tokenizerPath '+ bertpath+ '/latin.subword.encoder -f '+ a +'/' + txt +' -o  '+'./'+output+'/' +outfile , file = scriptfile )
		i=i+1

scriptfile.close()




for f in os.listdir('./' )
	nome=f.replace(" ", "_")
	os.rename(f,nome)

