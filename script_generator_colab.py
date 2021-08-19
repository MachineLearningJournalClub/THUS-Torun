import os
import argparse, sys


if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  parser.add_argument('-b', '--bertPath', help='path to pre-trained BERT', required=True)
  parser.add_argument('-t', '--tokenizerPath', help='path to Latin WordPiece tokenizer', required=True)
  
  parser.add_argument('-i','--sourcefile', help='text to analyze', required=True)

  parser.add_argument('-o','--outfile', help='File to write BERT representations to', required=True)


  args = vars(parser.parse_args())
  
  bertpath=args["bertPath"]
  encoder_path=args["tokenizerPath"]
  
  path=args['sourcefile']
  output=args["outfile"]



  if not os.path.exists(output):
    os.mkdir(output)

  scriptfile = open('script.sh', 'w')

  i=1

  for a,b,c in os.walk(path):
      for txt in c:

          print("echo ' ",i,' su ',len(os.listdir(path))," ' ",file = scriptfile)
      
          outfile=os.path.splitext(txt)[0]
      
          #print('python3 LatinBERT/text_to_pickle.py --bertPath '+ bertpath +' --tokenizerPath '+ encoder_path+ '/latin.subword.encoder -f '+ a + '/' + txt +' -o  '+'./'+output+'/' +outfile )
          
          print('python3 LatinBERT/text_to_pickle.py --bertPath '+ bertpath +' --tokenizerPath '+ encoder_path+ '/latin.subword.encoder -f '+ a + '/' + txt +' -o  '+'./'+output+'/' +outfile , file = scriptfile )
          i=i+1

  scriptfile.close()
