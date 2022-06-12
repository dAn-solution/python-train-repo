import numpy as np
import pandas as pd
import nibabel as nib
import matplotlib.pyplot as plt
from glob import glob

# get_df_allから呼び出される
# 受け取ったpathからfile名をDataFrameとして返す
def _get_df(base_path='public-covid-data', folder='rp_im'):
    data_dict = pd.DataFrame({'FilePath': glob('{}/{}/*'.format(base_path, folder)), 
                              'FileName': [p.split('/')[-1] for p in glob('{}/{}/*'.format(base_path, folder))]})
    return data_dict

# imとmaskのデータをファイル名でmergeする
def get_df_all(base_path='public-covid-data'):
    rp_im_df = _get_df(base_path, folder='rp_im')
    rp_msk_df = _get_df(base_path, folder='rp_msk')
    return rp_im_df.merge(rp_msk_df, on='FileName', suffixes=('Images', 'Mask'))


# NiftiデータをloadしてNumpyArrayにして、縦横を入れ替え
def load_nifti(path):
    data = nib.load(path)
    data = data.get_fdata()
    data = np.rollaxis(data, axis=1, start=0)
    return data


# マスクデータをRGBに色つけする
def label_color(mask_volume,
                ggo_color = [255, 0, 0],
                consolidation_color = [0, 255, 0],
                effusion_color = [0, 0, 255]):
    
    shp = mask_volume.shape
    # 箱作成
    mask_color = np.zeros((shp[0], shp[1], shp[2], 3), dtype=np.float32)
    # 色付け
    mask_color[np.equal(mask_volume, 1)] = ggo_color
    mask_color[np.equal(mask_volume, 2)] = consolidation_color
    mask_color[np.equal(mask_volume, 3)] = effusion_color

    return mask_color


# CTデータをHUスケールからグレースケールに変換する
def hu_to_gray(volume):
    maxhu = np.max(volume)
    minhu = np.min(volume)
    volume_rerange = (volume - minhu) / max((maxhu - minhu), 1e-3)
    volume_rerange = volume_rerange * 255
    volume_rerange = np.stack([volume_rerange, volume_rerange, volume_rerange], axis=-1)
    
    return volume_rerange.astype(np.uint8)


# CTデータとMASKデータをoverlayする
def overlay(gray_volune, mask_volume, mask_color, alpha=0.3):
    mask_filter = np.greater(mask_volume, 0)
    mask_filter = np.stack([mask_filter, mask_filter, mask_filter], axis=-1)
    # 病変ありなら計算、なしならCTデータを値をセット
    overlayed = np.where(mask_filter, 
                        ((1-alpha)*gray_volune + alpha*mask_color).astype(np.uint8), 
                        gray_volune)
    
    return overlayed


# スライスを並べて表示
def vis_overlay(overlayed, original_volume, mask_volume, cols = 5, display_num = 25, figsize=(15, 15)):
    
    rows = (display_num - 1) // cols + 1
    total_num = overlayed.shape[-2]
    interval = total_num / display_num
    if interval < 1:
        interval = 1
    fig, ax = plt.subplots(rows, cols, figsize=figsize)
    for i in range(display_num):
        row_i = i//cols
        cols_i = i%cols
        idx = int(i * interval)
        if idx >= total_num:
            break
        stats = get_hu_stats(original_volume[:, :, idx], mask_volume[:, :, idx])

        title = 'slice #: {}'.format(idx)
        title += '\nggo mean: {:.0f}±{:.0f}'.format(stats['ggo_mean'], stats['ggo_std'])
        title += '\nconsoli mean: {:.0f}±{:.0f}'.format(stats['consolidation_mean'], stats['consolidation_std'])
        title += '\neffusion mean: {:.0f}±{:.0f}'.format(stats['effusion_mean'], stats['effusion_std'])
        ax[row_i, cols_i].imshow(overlayed[:, :, idx])
        ax[row_i, cols_i].set_title(title)
        ax[row_i, cols_i].axis('off')
    fig.tight_layout()

    
# 枚数ごとの平均と標準偏差を計算
def get_hu_stats(volume, 
                  mask_volume, 
                  label_dict={1: 'ggo', 2: 'consolidation', 3: 'effusion'}):

    result = {}
    for label in label_dict.keys():
        prefix = label_dict[label]
        roi_hu = volume[np.equal(mask_volume, label)]
        result[prefix + '_mean'] = np.mean(roi_hu)
        result[prefix + '_std'] = np.std(roi_hu)

    return result