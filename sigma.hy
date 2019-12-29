(import [numpy :as np])
(import [itertools [chain]])

(defn get-range [expr]
  (setv ret {})
  (for [term expr]
    (setv name (first term))
    (for [(, ind var) (enumerate (rest term))]
      (if (not (.get ret var None))
        (assoc ret var `(get (. ~name shape) ~ind)))))
  ret)

(defn term-to-get [term]
  `(get ~(first term) (, ~@(rest term))))

(deftag Σ [expr]
  (setv new-term (first expr))
  (setv ranges (get-range (rest expr)))
  (setv outer-loop (set (rest new-term)))
  (setv inner-loop (- (set ranges) outer-loop))
  (setv new-var-name (first new-term))
  (setv new-var-shape (lfor ind outer-loop (get ranges ind)))
  (setv assign-stat `(setv ~new-var-name (np.zeros ~new-var-shape)))
  (setv loop-clause (list (chain.from_iterable (gfor (, x ran) (ranges.items) (, x `(range ~ran))))))
  (setv mul-clause `(* ~@(map term-to-get (rest expr))))
  `(do
    ~assign-stat
    (for ~loop-clause
      (+= ~(term-to-get new-term) ~mul-clause))))
