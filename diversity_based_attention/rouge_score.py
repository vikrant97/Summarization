from rouge import Rouge 

OUTPUT_DIR = "./output/"

rouge_1 = 0
rouge_2 = 0
rouge_l = 0
total_queries = 0

max_rouge_1 = -1.0
max_rouge_2 = -1.0
max_rouge_l = -1.0

tsentence = ["","",""]
psentence = ["","",""]

rouge = Rouge()

with open(OUTPUT_DIR + "test_final_results_plabels") as fp1, open(OUTPUT_DIR + "test_final_results_tlabels") as fp2:

	try:
		while(1):
			(plabel, garbage) = fp1.readline().split('<eos>')
			(tlabel, garbage) = fp2.readline().split('<eos>')

			scores = rouge.get_scores(tlabel, plabel)

			score = scores[0]
			rouge_1 += score['rouge-1']['f']
			rouge_2 += score['rouge-2']['f']
			rouge_l += score['rouge-l']['f']

			if score['rouge-1']['f'] > max_rouge_1:
				max_rouge_1 = score['rouge-1']['f']
				tsentence[0] = tlabel
				psentence[0] = plabel
			if score['rouge-2']['f'] > max_rouge_2:
				max_rouge_2 = score['rouge-2']['f']
				tsentence[1] = tlabel
				psentence[1] = plabel
			if score['rouge-l']['f'] > max_rouge_l:
				max_rouge_l = score['rouge-l']['f']
				tsentence[2] = tlabel
				psentence[2] = plabel

			total_queries += 1

	except :
		print("rouge-1: ", 100 * (rouge_1 / total_queries))
		print("rouge-2: ", 100 * (rouge_2 / total_queries))
		print("rouge-l: ", 100 * (rouge_l / total_queries))
		print("max rouge scores: ",max_rouge_1, max_rouge_2, max_rouge_l)
		print("ground truth")
		print(tsentence)
		print("predicted")
		print(psentence)
		print("Done")
