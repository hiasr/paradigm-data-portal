#!/usr/bin/env python3

from __future__ import annotations


from ctc.datasets import extract_native_transfers


output_dir = '/Users/stormslivkoff/repos/paradigm-data-portal/datasets/ethereum_native_transfers_raw'

extractor = extract_native_transfers.ExtractNativeTransfers(
    start_block=1_000,
    end_block=16_800_000,
    chunk_size=1000,
    output_dir=output_dir,
    tracker='file',
    output_filetype='csv',
    name='ethereum_native_transfers__v1_0_0',
    context={'network': 'ethereum'},
)

if __name__ == '__main__':
    extractor.orchestrate_jobs(executor='parallel')

