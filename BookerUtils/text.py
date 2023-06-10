import re
import xpinyin

def is_gbk(ch):
    try: 
        ch.encode('gbk')
        return True
    except:
        return False
        
def filter_gbk(fname):
    return ''.join([ch for ch in fname if is_gbk(ch)])

def gen_proj_name(name):
    # 转小写并移除扩展名
    name = re.sub(r'\.\w+$', '', name.lower())
    # 提取字母数字和中文，分别处理
    seg = re.findall(r'[\u4e00-\u9fff]+|[a-z0-9]+', name)
    nseg = []
    p = xpinyin.Pinyin()
    for s in seg:
        # 字母数字直接添加
        # 中文分词之后转拼音
        if re.search(r'[a-z0-9]', s):
            nseg.append(s)
        else:
            subseg = jieba.cut(s)
            for ss in subseg:
                nseg.append(p.get_pinyin(ss).replace('-', ''))
    res = '-'.join(nseg)
    # 数字开头的加上 x 
    if re.search(r'^\d', res): res = 'x' + res
    # 移除字母数字减号之外的所有字母
    res = re.sub(r'[^a-z0-9\-]', '', res)
    return res