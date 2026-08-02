# Deck structure: /paper-deck 1706.03762 --pages=10

Style preset assumed: journal-minimal. Language: Chinese. Raster image backend unavailable in this research workspace, so this is a simulated deck brief/outline, not a production PPTX.

## 01. Transformer in one sentence
- Role: cover
- Message: Transformer replaces recurrence/convolution with attention-only sequence transduction.
- Visual: clean architecture silhouette + attention arcs.
- Evidence: arXiv abstract; Figure 1.

## 02. Why recurrence bottlenecked sequence modeling
- Role: problem
- Message: Sequential computation limits parallel training and long-range dependency learning.
- Visual: RNN time chain vs parallel attention grid.
- Evidence: Introduction and Background.

## 03. Encoder-decoder blueprint
- Role: method-overview
- Message: Stacked encoder and decoder blocks are the core computational scaffold.
- Visual: left encoder stack, right decoder stack, source-to-target bridge.
- Evidence: Figure 1; Section 3.1.

## 04. Scaled dot-product attention
- Role: mechanism-detail
- Message: QK compatibility, sqrt(d_k) scaling, softmax, and weighted V sum form the attention primitive.
- Visual: matrix multiplication pipeline with formula callout.
- Evidence: Section 3.2.1; Figure 2.

## 05. Multi-head attention
- Role: mechanism-detail
- Message: Parallel heads preserve multiple relation subspaces and offset attention averaging.
- Visual: 8 heads as parallel lanes, concat, output projection.
- Evidence: Section 3.2.2.

## 06. Decoder masking and cross-attention
- Role: mechanism-detail
- Message: The decoder combines causal self-attention with attention over encoder outputs.
- Visual: triangular mask plus encoder-memory bridge.
- Evidence: Section 3.1 Decoder; Section 3.2.3.

## 07. Positional encoding
- Role: method-detail
- Message: Since attention has no recurrence, position is injected with sinusoidal encodings.
- Visual: token embeddings plus wave overlays.
- Evidence: Section 3.5.

## 08. Results and efficiency
- Role: evidence
- Message: WMT14 BLEU and training-time claims support the architecture.
- Visual: compact evidence cards: 28.4 En-De, 41.8 En-Fr, 3.5 days on 8 GPUs.
- Evidence: Abstract; Results Section 6.1.

## 09. What the paper changed
- Role: interpretation
- Message: The contribution is a new computational substrate: all-to-all differentiable routing.
- Visual: from sequential state machine to attention routing fabric.
- Evidence: verified interpretation from Sections 1-4, not a direct paper claim.

## 10. Fidelity checklist and takeaway
- Role: takeaway
- Message: A correct visual must show encoder/decoder asymmetry, masking, Q/K/V, scaling, multi-head concat, and positional encoding.
- Visual: checklist over a simplified architecture.
- Evidence: derived from Sections 3.1-3.5.
