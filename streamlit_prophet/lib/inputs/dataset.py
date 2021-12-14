from typing import Any, Dict, Tuple

import pandas as pd
import streamlit as st
from streamlit_prophet.lib.exposition.export import display_config_download_links
from streamlit_prophet.lib.utils.load import download_toy_dataset, load_custom_config, load_dataset


def input_dataset(
    config: Dict[Any, Any], readme: Dict[Any, Any], instructions: Dict[Any, Any]
) -> Tuple[pd.DataFrame, Dict[Any, Any], Dict[Any, Any], Dict[Any, Any]]:
    """Lets the user decide whether to upload a dataset or download a toy dataset.

    Parameters
    ----------
    config : Dict
        Lib config dictionary containing information about toy datasets (download links).
    readme : Dict
        Dictionary containing tooltips to guide user's choices.
    instructions : Dict
        Dictionary containing instructions to provide a custom config.

    Returns
    -------
    pd.DataFrame
        Selected dataset loaded into a dataframe.
    dict
        Loading options selected by user (upload or download, dataset name if download).
    dict
        Lib configuration dictionary.
    dict
        Dictionary containing all datasets.
   
    load_options, datasets = dict(), dict()

    
    load_options["toy_dataset"]:
        dataset_name = st.selectbox(
            "Select your dataset",
            options=list(config["datasets"].keys()),
            format_func=lambda x: config["datasets"][x]["name"],
            help=readme["tooltips"]["toy_dataset"],
        )
       """
