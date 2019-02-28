from fastai.text import *
import html


LM_PATH=Path('data/sent_lm/')
re1 = re.compile(r'  +')
BOS = 'xbos'  # beginning-of-sentence tag
FLD = 'xfld'  # data field tag
itos = pickle.load(open(f'{LM_PATH}/tmp/itos.pkl', 'rb'))
stoi = collections.defaultdict(lambda:0, {v:k for k,v in enumerate(itos)})



def fixup(x):
    x = x.replace('#39;', "'").replace('amp;', '&').replace('#146;', "'").replace(
        'nbsp;', ' ').replace('#36;', '$').replace('\\n', "\n").replace('quot;', "'").replace(
        '<br />', "\n").replace('\\"', '"').replace('<unk>','u_n').replace(' @.@ ','.').replace(
        ' @-@ ','-').replace('\\', ' \\ ')
    return re1.sub(' ', html.unescape(x))
    
def get_texts(df):
    texts = f'\n{BOS} {FLD} 1 ' + df['text'].astype(str)
    for i in range(1, len(df.columns)): texts += f' {FLD} {i-n_lbls} ' + df[i].astype(str)
    texts = list(texts.apply(fixup).values)

    tok = Tokenizer().proc_all_mp(partition_by_cores(texts))
    return tok

def get_all(df):
    tok=[]
    for i, r in enumerate(df):
        tok_= get_texts(r)
        tok += tok_;
    return tok

def numericalise(text):
    return(np.array([stoi[n] for n in np.array(text)[0].tolist()]))
