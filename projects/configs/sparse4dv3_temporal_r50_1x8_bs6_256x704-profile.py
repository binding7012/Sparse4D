_base_ = [
    './sparse4dv3_temporal_r50_1x8_bs6_256x704.py',
]

custom_imports = dict(
    imports=['my_hooks.profiler_hook'],
    allow_failed_imports=False
)

custom_hooks = [
    dict(
        type='MyProfilerHook',
        log_dir='./profiler_logs',
        profile_step_start=305,
        profile_step_end=306,
        priority='VERY_HIGH'
    )
]
