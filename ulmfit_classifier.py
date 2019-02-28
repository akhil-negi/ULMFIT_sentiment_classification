from helper import *

class ulmfit_classifier:
    def __init__(self):


        PATH=Path('data/sent/')
        DATA_PATH=Path('data/')
        CLAS_PATH=Path('data/sent_clas/')
        MODEL_NAME='clas_final'
        LM_PATH=Path('data/sent_lm/')


        with (CLAS_PATH/'classes.txt').open('r') as f:
            clas_list=f.readlines()
            self.clas_dict={i:o.replace('\n','') for i,o in enumerate(clas_list)}





        bptt,em_sz,nh,nl = 70,400,1150,3
        vs = len(itos)
        opt_fn = partial(optim.Adam, betas=(0.8, 0.99))
        bs = 48
        c=3

        dps = np.array([0.4,0.5,0.05,0.3,0.4])*0.5

        self.m = get_rnn_classifer(bptt, 20*70, c, vs, emb_sz=em_sz, n_hid=nh, n_layers=nl, pad_token=1,
                  layers=[em_sz*3, 50, c], drops=[dps[4], 0.1],
                  dropouti=dps[0], wdrop=dps[1], dropoute=dps[2], dropouth=dps[3])
        opt_fn = partial(optim.Adam, betas=(0.7, 0.99)) 

        md = ModelData(PATH, trn_dl=[], val_dl=[])

        self.learn = RNN_Learner(md, TextModel(to_gpu(self.m)), opt_fn=opt_fn)
        self.learn.reg_fn = partial(seq2seq_reg, alpha=2, beta=1)
        self.learn.clip=.25
        self.learn.metrics = [accuracy]
        self.learn.load(MODEL_NAME)

    def predict(self,inpt):
        BOS = 'xbos'  # beginning-of-sentence tag
        FLD = 'xfld'  # data field tag
        df_test=pd.read_json(json.dumps(inpt),lines=True,chunksize = 1)
        text=get_all(df_test)
        self.m.reset()
        return self.clas_dict[np.argmax(self.learn.predict_array(numericalise(text).reshape(-1,1))[0])]

