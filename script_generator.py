import os

path='library_super_reduced' 
bertpath='/latin_bert' 
output='pickle'



if not os.path.exists(output):
  os.mkdir(output)

scriptfile = open('script.sh', 'w')

i=1

for a,b,c in os.walk(path):
	for txt in c:

		print("echo ' ",i,' su ',len(os.listdir(path))," ' ",file = scriptfile)
	
		outfile=os.path.splitext(txt)[0]
	
		#print('python3 ./gen_file2.py --bertPath '+ bertpath +' --tokenizerPath '+ bertpath+ '/latin.subword.encoder -f '+ path +'/'+ b +'/' + txt +' -o  '+'/'+output+'/' +outfile , file = scriptfile )
		print('python3 ./text_to_pickle.py --bertPath '+ bertpath +' --tokenizerPath '+ bertpath+ '/latin.subword.encoder -f '+ a +'/' + txt +' -o  '+'./'+output+'/' +outfile , file = scriptfile )
		i=i+1

scriptfile.close()
