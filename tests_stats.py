import pandas as pd
import math


def aggregate_resuls1(file_path, sparator):
    df = pd.read_csv(file_path, sep=sparator, header=None)
    df.columns = ['alg', 'number', 'ans', 'corr_ans', 'times']

    sums = []
    for time in df["times"]:
        s = [float(t) for t in time[1:-1].replace(" ", "").split(",")]
        # print(time[1:-1].replace(" ", "").split(","), math.fsum(s))
        sums.append(math.fsum(s))
    df["stimes"] = sums

    is_corres = []
    for corr_ans, abs in zip(df['corr_ans'], df['ans']):
        # print(corr_ans[1:-1].replace(" ", "").split(","), abs[1:-1].replace(" ", "").split(","), set(corr_ans[1:-1].replace(" ", "").split(","))== set(abs[1:-1].replace(" ", "").split(",")))
        is_corres.append(set(corr_ans[1:-1].replace(" ", "").split(","))
                         == set(abs[1:-1].replace(" ", "").split(",")))
    df["is_corr"] = is_corres

    df['not_corr'] = df['is_corr']

    data_aggregated = df.groupby(by=["alg"], as_index=False).agg({'stimes': 'mean',
                                                                  'is_corr': 'sum',
                                                                  'not_corr': 'count'})
    data_aggregated.columns = ['alg', 'avg_time', "correct ans", "all ans"]
    data_aggregated['accuracy'] = data_aggregated['correct ans'] / \
        data_aggregated['all ans'] * 100
    return data_aggregated


def aggregate_resuls2(file_path, sparator):
    df = pd.read_csv(file_path, sep=sparator, header=None)
    df.columns = ['alg', 'number', 'ans', 'corr_ans', 'times']

    sums = []
    for time in df["times"]:
        s = [float(t) for t in time[1:-1].replace(" ", "").split(",")]
        # print(time[1:-1].replace(" ", "").split(","), math.fsum(s))
        sums.append(math.fsum(s))
    df["stimes"] = sums

    is_corres = []
    for corr_ans, abs in zip(df['corr_ans'], df['ans']):
        # print(corr_ans[1:-1].replace(" ", "").split(","), abs[1:-1].replace(" ", "").split(","), set(corr_ans[1:-1].replace(" ", "").split(","))== set(abs[1:-1].replace(" ", "").split(",")))
        is_corres.append(set(corr_ans[1:-1].replace(" ", "").split(","))
                         == set(abs[1:-1].replace(" ", "").split(",")))
    df["is_corr"] = is_corres

    df['not_corr'] = df['is_corr']

    data_aggregated2 = df.groupby(by=["alg", "number"], as_index=False).agg({'stimes': 'mean',
                                                                            'is_corr': 'sum',
                                                                             'not_corr': 'count'})
    data_aggregated2.columns = ['alg', 'number',
                                'avg_time', "correct ans", "all ans"]
    data_aggregated2['accuracy'] = data_aggregated2['correct ans'] / \
        data_aggregated2['all ans'] * 100
    return data_aggregated2
