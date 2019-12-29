(import [numpy :as np])
(require [sigma [Σ]])

(defn matmul [a b]
  #Σ[(c i k) (a i j) (b j k)]
  c)

(defn ntn [x y w wb bias]
  #Σ[(s1 k) (x i) (y j) (w i j k)]
  (setv xy (np.concatenate [x y]))
  #Σ[(s2 k) (wb k i) (xy i)]
  (+ s1 s2 bias))
