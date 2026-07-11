# xu-l20 FineTune to huashan FineTune_only Sync

- Timestamp: 2026-07-07 23:20 +0800
- Source: `xu-l20:/data/chenjt/hate/FineTune`
- Destination: `huashan:/data/chenjt/Hate/FineTune_only`
- Reason: user requested syncing the latest and most complete FineTune experiment workspace from `xu-l20` to `huashan`.

## Pre-Sync State

- Source size: `4.7G`
- Source file count: `1022`
- Source byte sum: `5001442927`
- Existing destination size: `1.4G`
- Existing destination file count: `261`
- Existing destination byte sum: `1443940130`
- huashan `/data` free space before sync: approximately `5.1T`

## Transfer Method

`huashan` could not resolve the local SSH alias `xu-l20`, so the transfer used the local machine as a temporary relay:

1. Streamed `xu-l20:/data/chenjt/hate/FineTune/` into local temporary directory:
   - `tmp/remote-sync/20260707-xu-l20-FineTune-to-huashan/FineTune/`
2. Verified local temporary copy:
   - file count: `1022`
   - byte sum: `5001442927`
3. Renamed existing huashan destination to:
   - `/data/chenjt/Hate/FineTune_only.pre_xu_l20_sync_20260707_232011`
4. Uploaded the verified local temporary copy to:
   - `/data/chenjt/Hate/FineTune_only/`

## Post-Sync Verification

Source:

- `xu-l20:/data/chenjt/hate/FineTune`
- file count: `1022`
- byte sum: `5001442927`
- size: `4.7G`

Destination:

- `huashan:/data/chenjt/Hate/FineTune_only`
- file count: `1022`
- byte sum: `5001442927`
- size: `4.7G`

The old huashan destination remains available at:

- `huashan:/data/chenjt/Hate/FineTune_only.pre_xu_l20_sync_20260707_232011`

## Notes

- This was a full replacement-by-backup workflow, not an in-place destructive delete.
- The local temporary relay copy is under ignored `tmp/` and can be removed after the sync no longer needs local transfer evidence.
