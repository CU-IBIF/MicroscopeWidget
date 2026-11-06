# Copyright (c) 2026, Creighton University
# SPDX-License-Identifier: BSD-3-Clause
#
# DISCLAIMER: This software is provided "AS IS", without warranty or guarantee
# of any kind, express or implied, including but not limited to merchantability,
# fitness for a particular purpose, accuracy, and non-infringement. It is NOT FIT
# FOR ANY PURPOSE, STATED OR IMPLIED. It is a simplified educational model, not
# intended for clinical, diagnostic, or regulatory use or for the operation of
# any real instrument; its results may be wrong and must be independently
# verified. In no event shall Creighton University or the contributors be liable
# for any claim, damages, or other liability arising from its use. See LICENSE.

import os

# Qt must be told to run headless before QApplication is constructed.
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")

import pytest


@pytest.fixture(autouse=True)
def isolated_progress(tmp_path, monkeypatch):
    """Keep the test run out of the player's real save file.

    Progress lives in the per-user config directory, so a test that solves a round
    was writing into whoever ran the suite -- and reading their history back in,
    which made carry-forward tests depend on what a previous run had left behind.
    """
    from microscopevuilder.game import progress as progress_module

    save = tmp_path / "progress.json"
    monkeypatch.setattr(progress_module, "default_save_path", lambda: save)
    return save
