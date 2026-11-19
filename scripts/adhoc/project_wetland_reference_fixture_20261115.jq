# Purpose: project actual471 reference metadata for public contract controls.
# Inputs: --slurpfile measurement/start/receipt/shell/references; outputs stdout.
# No source bodies; runtime/cache breadth omitted only in this test fixture.
# Serves issue2910, 2026-11-15; actual full raw artifacts remain immutable.
def head_projection:
  {revision,source_state,target,after_sha256,
   input_sha256:{(.target):.input_sha256[.target]},
   implementation_sha256:{},plan,interpretation,started_at};
def shell_projection:
  {name,command,started_at,head,finished_at,exit_code,status,log_sha256,log_bytes};
{
  provenance: {
    scope:"Projection of the actual successful16/16 record measurement; source/cache breadth and interpreter paths omitted only from this contract-test fixture.",
    measurement_raw_sha256:"67e3eb1c897816c9addac3e6ed965be2ceaa9d7d02c0c6d00bd983b0b4e27bd2",
    receipt_raw_sha256:"b732bce00d977fc12ac3a3e4fdbb854a4ae47b311e12726380176e87ac5d84f7"
  },
  directory:".temp/gtdb-wetland-identity-20261115/reference-measurement-001",
  started:($start[0]|head_projection),
  receipt:($receipt[0]|head_projection + {finished_at,inputs_unchanged,measurement_sha256,log_sha256,exit_code,counts}),
  measurement:$measurement[0],
  shell:($shell[0]|shell_projection),
  references:($references[0]|shell_projection)
}
